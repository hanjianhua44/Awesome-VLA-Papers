"""Render and send the ranked daily paper digest as an HTML email."""
from __future__ import annotations

import html
import os
import smtplib
import ssl
import tempfile
import time
from pathlib import Path
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

DEFAULT_FROM = "hanjianhua44@163.com"
DEFAULT_TO = "hanjianhua4@huawei.com"
DEFAULT_NAME = "波士顿大龙虾"


def _environment_value(name: str, default: str = "") -> str:
    """Read process env, with a Windows user-env fallback for scheduled tasks."""
    value = os.getenv(name)
    if value is not None:
        return value
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                return str(winreg.QueryValueEx(key, name)[0])
        except (FileNotFoundError, OSError):
            pass
    return default


def _short_summary(abstract: str, limit: int = 320) -> str:
    text = " ".join((abstract or "").split())
    if len(text) <= limit:
        return text
    boundary = text.rfind(" ", 0, limit)
    return text[: boundary if boundary > 180 else limit].rstrip() + "…"


def render_digest_html(
    papers: list[dict],
    date_str: str,
    cover_str: str,
    report_url: str = "",
    sync_ok: bool = True,
    include_paper_links: bool = True,
) -> str:
    """Build an email-client-friendly digest with inline CSS only."""
    cards = []
    for index, paper in enumerate(papers, 1):
        title = html.escape(paper.get("title", "Untitled"))
        url = html.escape(paper.get("url", ""), quote=True)
        institution = html.escape(paper.get("institution", "—"))
        topic = html.escape(
            paper.get("curated_topic_label")
            or paper.get("curated_topic")
            or "VLA / Embodied AI"
        )
        summary = html.escape(_short_summary(paper.get("abstract", "")))
        score = float(paper.get("final_score", paper.get("score", 0)))
        if include_paper_links:
            title_html = (
                f'<a href="{url}" style="font-size:16px;font-weight:700;'
                f'color:#175cd3;text-decoration:none">{title}</a>'
            )
        else:
            title_html = (
                f'<div style="font-size:16px;font-weight:700;color:#101828">'
                f"{title}</div>"
            )
        cards.append(
            f"""
            <tr><td style="padding:0 0 14px">
              <div style="border:1px solid #e4e7ec;border-radius:10px;padding:14px 16px;background:#fff">
                <div style="font-size:12px;color:#667085;margin-bottom:5px">
                  #{index} · {topic} · score {score:.2f}
                </div>
                {title_html}
                <div style="font-size:13px;color:#475467;margin:7px 0">{institution}</div>
                <div style="font-size:14px;line-height:1.65;color:#344054">{summary}</div>
              </div>
            </td></tr>"""
        )

    status = (
        "GitHub 日报已同步"
        if sync_ok
        else "GitHub 同步失败，但完整筛选结果仍随邮件送达"
    )
    report_link = (
        f'<a href="{html.escape(report_url, quote=True)}" style="color:#175cd3">查看 GitHub 日报</a>'
        if report_url else ""
    )
    return f"""<!doctype html>
<html><body style="margin:0;background:#f7f8fa;font-family:Arial,'Microsoft YaHei',sans-serif;color:#101828">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
    <tr><td align="center" style="padding:24px 12px">
      <table role="presentation" width="680" style="max-width:100%" cellspacing="0" cellpadding="0">
        <tr><td style="padding:22px;border-radius:12px;background:#101828;color:#fff">
          <div style="font-size:12px;color:#b2ccff">Awesome VLA Papers · {html.escape(date_str)}</div>
          <h1 style="font-size:24px;margin:7px 0 5px">今日精选 {len(papers)} 篇</h1>
          <div style="font-size:14px;color:#d0d5dd">覆盖 {html.escape(cover_str)} · {status}</div>
        </td></tr>
        <tr><td style="padding:14px 2px 8px;font-size:14px;color:#475467">
          按首页 Topic 相似度、研究相关性、机构质量与内容多样性综合排序。{report_link}
        </td></tr>
        {''.join(cards)}
        <tr><td style="padding:12px 4px;color:#667085;font-size:13px;line-height:1.6">
          ——<br>波士顿大龙虾主管<br>
          “重要的不是预测未来，而是让未来成为可能。” —— 《小王子》式的科研浪漫
        </td></tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def render_digest_text(
    papers: list[dict],
    date_str: str,
    cover_str: str,
    report_url: str = "",
    include_links: bool = False,
) -> str:
    domain_labels = {
        "ad": "AUTONOMOUS DRIVING",
        "robot": "ROBOTICS & EMBODIED AI",
        "general": "GENERAL / CROSS-DOMAIN",
    }
    grouped = {domain: [] for domain in domain_labels}
    for paper in papers:
        grouped.setdefault(paper.get("selection_domain", "general"), []).append(paper)

    lines = [
        "AWESOME VLA PAPERS",
        f"Daily Research Brief  |  {date_str}",
        "=" * 68,
        f"Coverage: {cover_str}",
        f"Selection: {len(papers)} papers ranked by topic relevance, institution, and diversity",
        "",
    ]
    if report_url:
        lines.extend([
            "Full report, abstracts, and paper links:",
            report_url,
            "",
        ])

    number = 1
    for domain in ("ad", "robot", "general"):
        domain_papers = grouped.get(domain, [])
        if not domain_papers:
            continue
        lines.extend([
            f"[{domain_labels[domain]}]  {len(domain_papers)} papers",
            "-" * 68,
        ])
        for paper in domain_papers:
            topic = paper.get(
                "curated_topic_label",
                paper.get("curated_topic", "VLA / Embodied AI"),
            )
            score = float(paper.get("final_score", paper.get("score", 0)))
            lines.extend([
                f"{number:02d}. {paper.get('title', 'Untitled')}",
                f"    Institution : {paper.get('institution', '—')}",
                f"    Topic       : {topic}",
                f"    arXiv       : {paper.get('arxiv_id', '')}    Relevance: {score:.2f}",
                f"    Brief       : {_short_summary(paper.get('abstract', ''), 260)}",
            ])
            if include_links and paper.get("url"):
                lines.append(f"    Paper       : {paper['url']}")
            lines.append("")
            number += 1

    lines.extend([
        "=" * 68,
        "Method: homepage Topic similarity + research relevance + institution",
        "quality + diversity constraints. Autonomous driving reserves at least",
        "three slots when enough qualifying candidates are available.",
        "",
        "Awesome VLA Papers Research Digest",
    ])
    return "\n".join(lines)


def send_digest(
    papers: list[dict],
    date_str: str,
    cover_str: str,
    report_url: str = "",
    sync_ok: bool = True,
    retries: int = 3,
    subject_prefix: str = "",
) -> None:
    """Send the digest using SMTP credentials from environment variables."""
    smtp_host = _environment_value("SMTP_HOST", "smtp.163.com")
    smtp_port = int(_environment_value("SMTP_PORT", "465"))
    smtp_user = _environment_value("SMTP_USER", DEFAULT_FROM)
    smtp_password = _environment_value("SMTP_AUTH_CODE").strip()
    recipient = _environment_value("DIGEST_TO", DEFAULT_TO)
    display_name = _environment_value("SMTP_DISPLAY_NAME", DEFAULT_NAME)
    if not smtp_password:
        raise RuntimeError("SMTP_AUTH_CODE is not configured")

    email_mode = _environment_value("DIGEST_EMAIL_MODE", "pdf").strip().lower()
    include_links = email_mode == "html"
    body = render_digest_html(
        papers,
        date_str,
        cover_str,
        report_url,
        sync_ok,
        include_paper_links=include_links,
    )
    text_body = render_digest_text(
        papers, date_str, cover_str, report_url, include_links=include_links
    )
    if email_mode == "pdf":
        from render_digest_pdf import build_digest_pdf

        message = MIMEMultipart("mixed")
        message.attach(MIMEText(
            f"Today's Awesome VLA Research Brief is attached as a PDF.\n"
            f"{len(papers)} selected papers covering {cover_str}.",
            "plain",
            "utf-8",
        ))
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = Path(directory) / f"awesome-vla-digest-{date_str}.pdf"
            build_digest_pdf(papers, date_str, cover_str, report_url, pdf_path)
            attachment = MIMEApplication(
                pdf_path.read_bytes(),
                _subtype="pdf",
            )
        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=f"awesome-vla-digest-{date_str}.pdf",
        )
        message.attach(attachment)
    elif email_mode in {"html", "html-lite"}:
        message = MIMEMultipart("alternative")
        message.attach(MIMEText(text_body, "plain", "utf-8"))
        message.attach(MIMEText(body, "html", "utf-8"))
    else:
        message = MIMEText(text_body, "plain", "utf-8")
    message["From"] = formataddr((str(Header(display_name, "utf-8")), smtp_user))
    message["To"] = recipient
    prefix = f"{subject_prefix.strip()} " if subject_prefix.strip() else ""
    message["Subject"] = Header(
        f"{prefix}Awesome VLA Research Brief｜{date_str}｜{len(papers)} papers",
        "utf-8",
    )

    context = ssl.create_default_context()
    for attempt in range(1, retries + 1):
        try:
            with smtplib.SMTP_SSL(
                smtp_host, smtp_port, context=context, timeout=30
            ) as server:
                server.login(smtp_user, smtp_password)
                refused = server.sendmail(
                    smtp_user, [recipient], message.as_string()
                )
                if refused:
                    raise RuntimeError(f"SMTP refused recipients: {list(refused)}")
            return
        except Exception:
            if attempt >= retries:
                raise
            time.sleep(5 * attempt)

