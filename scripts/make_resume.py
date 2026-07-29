#!/usr/bin/env python3
"""Generate Sudi David's resume PDF for the portfolio site."""

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from pathlib import Path

OUT = str(Path(__file__).resolve().parent.parent / "public" / "Sudi-David-Resume.pdf")

INK = HexColor("#111318")
BODY = HexColor("#3f4450")
MUTED = HexColor("#8a8f9c")
ACCENT = HexColor("#5b6fb5")
RULE = HexColor("#e3e5ea")

styles = {
    "name": ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=INK
    ),
    "role": ParagraphStyle(
        "role", fontName="Helvetica", fontSize=11, leading=14, textColor=ACCENT
    ),
    "contact": ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MUTED
    ),
    "summary": ParagraphStyle(
        "summary", fontName="Helvetica", fontSize=9.5, leading=14.5, textColor=BODY
    ),
    "section": ParagraphStyle(
        "section",
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=MUTED,
        spaceBefore=0,
    ),
    "job_title": ParagraphStyle(
        "job_title", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK
    ),
    "job_meta": ParagraphStyle(
        "job_meta", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MUTED
    ),
    "period": ParagraphStyle(
        "period",
        fontName="Helvetica",
        fontSize=8.5,
        leading=13,
        textColor=MUTED,
        alignment=2,
    ),
    "bullet": ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9,
        leading=13.5,
        textColor=BODY,
        leftIndent=9,
        bulletIndent=0,
        alignment=TA_LEFT,
    ),
    "plain": ParagraphStyle(
        "plain", fontName="Helvetica", fontSize=9, leading=13.5, textColor=BODY
    ),
}


def letterspace(text: str) -> str:
    return "&nbsp;".join(text)


def section(title: str):
    return [
        Spacer(1, 6.5 * mm),
        Paragraph(letterspace(title), styles["section"]),
        Spacer(1, 1.5 * mm),
        HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=3 * mm),
    ]


def job(title, company, location, period, bullets):
    left = Paragraph(title, styles["job_title"])
    right = Paragraph(period, styles["period"])
    head = Table([[left, right]], colWidths=[118 * mm, 52 * mm])
    head.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    meta = f'<font color="#5b6fb5"><b>{company}</b></font>'
    if location:
        meta += f'&nbsp;&nbsp;·&nbsp;&nbsp;{location}'
    flow = [head, Paragraph(meta, styles["job_meta"]), Spacer(1, 1.6 * mm)]
    for b in bullets:
        flow.append(Paragraph(b, styles["bullet"], bulletText="–"))
        flow.append(Spacer(1, 0.9 * mm))
    flow.append(Spacer(1, 2.6 * mm))
    return flow


doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=16 * mm,
    bottomMargin=14 * mm,
    title="Sudi David — Resume",
    author="Sudi David",
)

story = []

story.append(Paragraph("Sudi David", styles["name"]))
story.append(Spacer(1, 1.2 * mm))
story.append(Paragraph("Full-Stack Software Engineer", styles["role"]))
story.append(Spacer(1, 2.4 * mm))
story.append(
    Paragraph(
        "contact@sudi.dev&nbsp;&nbsp;·&nbsp;&nbsp;+243 817 334 881&nbsp;&nbsp;·&nbsp;&nbsp;"
        "github.com/SudiDav&nbsp;&nbsp;·&nbsp;&nbsp;sudi.dev/blog&nbsp;&nbsp;·&nbsp;&nbsp;DRC",
        styles["contact"],
    )
)
story.append(Spacer(1, 3.4 * mm))
story.append(
    Paragraph(
        "Full-Stack Software Engineer with 9+ years of experience building high-performance, "
        "scalable backend systems. Proven track record delivering end-to-end solutions across "
        "fintech, edtech, and enterprise domains. Skilled in leading distributed teams, mentoring "
        "junior developers, and turning complex technical challenges into reliable, "
        "production-ready software.",
        styles["summary"],
    )
)

story += section("WORK EXPERIENCE")
story += job(
    "Senior Software Engineer",
    "Almafrica",
    "",
    "May 2026 — Present",
    [
        "Architected and designed the mobile app, frontend, and backend of a platform helping farmers join the world of tech (almafrica.com).",
        "Leading a team of developers and mentoring junior engineers.",
    ],
)
story += job(
    "FullStack Engineer",
    "IST Africa",
    "Remote, Denmark",
    "Feb 2024 — Apr 2026",
    [
        "Spearheaded the redevelopment of a comprehensive school management system tailored for Danish schools, starting with the Absence module.",
        "Coordinated effectively with distributed teams across different regions, ensuring smooth communication and project delivery.",
        "Utilized modern technologies and frameworks to deliver a high-performance, future-proof school management system.",
    ],
)
story += job(
    "FullStack Engineer",
    "Altech Group",
    "DRC (Hybrid)",
    "Feb 2021 — Jan 2024",
    [
        "Managed a team of 4 developers and collaborated with different departments on the integration of a loan asset management system, successfully launched.",
        "Improved business processes by integrating third-party solutions like Spark Energy and Omnivoltaic.",
        "Worked with the finance team to streamline workloads by integrating the Xero and Telerivet APIs, helping both customers and the finance team.",
    ],
)
story += job(
    "FullStack Engineer",
    "Fintech Group",
    "Uganda",
    "Apr 2018 — Dec 2019",
    [
        "Built a reporting system for AB Bank integrated into CHEQUEPOINT, reducing paperwork on the user's side by 70%.",
        "Automated file generation at NCBA bank from the CHEQUEPOINT system to the core banking system.",
        "Reduced hands-on financial reconciliations by integrating a web service to check account balances from the core banking system.",
    ],
)
story += job(
    "FullStack Engineer",
    "Fintech Group",
    "Uganda",
    "Feb 2017 — Mar 2018",
    [
        "Integrated the central bank system with various banks through CHEQUEPOINT, a web application bridging local banks and the central bank.",
        "Migrated the legacy system to MSSQL and ASP.NET web forms and web services, helping users work confidently with 85% fewer errors.",
    ],
)

story += section("EDUCATION")
story.append(
    Paragraph(
        "<b>Sikkim Manipal University</b> — Degree in Science of Information Technology",
        styles["plain"],
    )
)
story.append(Spacer(1, 0.8 * mm))
story.append(
    Paragraph("Kampala, Uganda · 2013 — 2017 · Top 10% of my class", styles["job_meta"])
)

story += section("PROJECT")
story.append(
    Paragraph(
        "<b>Auction Car Web App</b> — Microservices .NET web application built with RabbitMQ, Docker, and Kubernetes.",
        styles["plain"],
    )
)

story += section("TECHNOLOGIES")
story.append(
    Paragraph(
        "<b>Stack:</b> .NET C#, ASP.NET Core, TypeScript, NodeJS, NestJS, React, Vue, "
        "Entity Framework Core, TypeORM, Mongoose",
        styles["plain"],
    )
)
story.append(Spacer(1, 1.2 * mm))
story.append(
    Paragraph(
        "<b>Other:</b> SQL Server, MongoDB, PostgreSQL, RabbitMQ, AWS (EC2, S3), REST API, "
        "GraphQL, DigitalOcean, Nginx, Traefik, Docker, Docker Swarm, Bash, JIRA, Cloudflare, "
        "GitHub Actions, Jenkins, OpenTelemetry, Datadog, Sentry, Microservices Architecture",
        styles["plain"],
    )
)

story += section("AWARDS")
story.append(
    Paragraph(
        "<b>Facebook Developer Challenge (2018)</b> — Built JusticeBot, a chatbot that provides "
        "legal procedure information in a simplified manner and connects users with legal service "
        "providers for free.",
        styles["plain"],
    )
)

story += section("LANGUAGES")
story.append(
    Paragraph(
        "Swahili (native)&nbsp;&nbsp;·&nbsp;&nbsp;French (native)&nbsp;&nbsp;·&nbsp;&nbsp;English (C2, fluent)",
        styles["plain"],
    )
)

doc.build(story)
print("PDF written to", OUT)
