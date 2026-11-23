# Shared content for the LEGO case study: used by app.py (Streamlit) and build_preview.py (static preview)
RED, YEL, BLUE, GREEN, DARK, PALE = "#5741D9", "#F5B841", "#1B1340", "#12A594", "#1B1340", "#F1EEFE"
TABCOL = [RED, YEL, BLUE, GREEN]

CSS = f"""
.cs {{ font-family: 'Helvetica Neue', Arial, sans-serif; color:#1F1F24; max-width:1150px; margin:0 auto; }}
.cs p, .cs li {{ line-height:1.6; color:#1F1F24; }}
.cs .banner {{ background:{RED}; border-radius:14px 14px 0 0; padding:1.8rem 2.2rem 1.5rem; position:relative; overflow:hidden; }}
.cs .stripe {{ height:8px; background:{YEL}; border-radius:0 0 14px 14px; margin-bottom:1.2rem; }}
.cs .tag {{ display:inline-block; background:{YEL}; color:#3A2A00 !important; font-weight:700; font-size:0.78rem; letter-spacing:0.05em; text-transform:uppercase; padding:0.25rem 0.75rem; border-radius:999px; }}
.cs .btitle {{ color:#FFFFFF !important; font-size:2.1rem; font-weight:800; margin:0.7rem 0 0.4rem; line-height:1.2; max-width:640px; }}
.cs .bsub {{ color:#E4DEFF !important; font-size:1.05rem; max-width:640px; }}
.cs .by {{ color:#FFFFFF !important; margin-top:1rem; font-size:0.95rem; }}
.cs .by a {{ color:{YEL} !important; text-decoration:none; font-weight:700; }}
.cs .bricks {{ position:absolute; right:26px; top:22px; width:300px; height:150px; }}
.cs .brick {{ position:absolute; border-radius:5px; }}
.cs .stud {{ position:absolute; top:-9px; width:17px; height:9px; border-radius:4px 4px 0 0; }}
.cs .kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:0.9rem; margin:0 0 1.2rem; }}
.cs .kpi {{ background:{PALE}; border-top:6px solid {RED}; border-radius:8px; padding:0.9rem 1rem; }}
.cs .kpi .v {{ font-size:1.7rem; font-weight:800; color:#2A1B6E !important; }}
.cs .kpi .l {{ font-size:0.85rem; color:#4B4470 !important; }}
.cs .nav {{ display:flex; flex-wrap:wrap; gap:0.45rem; margin:0 0 1.4rem; }}
.cs .nav a {{ text-decoration:none; font-weight:700; font-size:0.86rem; padding:0.5rem 0.85rem; border-radius:8px; }}
.cs .block {{ border:1px solid #E1DBFB; border-radius:12px; overflow:hidden; margin:0 0 1.6rem; background:#FFFFFF; scroll-margin-top:70px; }}
.cs .bh {{ padding:0.7rem 1.1rem; font-weight:800; font-size:1.05rem; }}
.cs .bh small {{ display:block; font-weight:700; font-size:0.72rem; letter-spacing:0.12em; opacity:0.85; }}
.cs .bb {{ padding:1rem 1.2rem 1.1rem; }}
.cs .cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:0.8rem; margin:0.4rem 0 0.9rem; }}
.cs .cards.two {{ grid-template-columns:repeat(2,1fr); }}
.cs .cards.four {{ grid-template-columns:repeat(4,1fr); }}
.cs .card {{ background:#FFFFFF; border:1px solid #ECECEC; border-top:5px solid {BLUE}; border-radius:8px; padding:0.8rem 0.9rem; }}
.cs .card h4 {{ margin:0 0 0.35rem; font-size:0.98rem; color:#14213D !important; }}
.cs .card div, .cs .card li {{ font-size:0.9rem; color:#3A4250 !important; }}
.cs .card ul {{ margin:0; padding-left:1.1rem; }}
.cs table.t {{ width:100%; border-collapse:collapse; margin:0.3rem 0 0.9rem; font-size:0.92rem; }}
.cs table.t th {{ background:{DARK}; color:#FFFFFF !important; text-align:left; padding:0.55rem 0.7rem; }}
.cs table.t td {{ border-bottom:1px solid #EEE; padding:0.55rem 0.7rem; vertical-align:top; color:#1F1F24 !important; }}
.cs table.t tr:nth-child(even) td {{ background:{PALE}; }}
.cs .note {{ background:{PALE}; border-left:5px solid {YEL}; padding:0.75rem 1rem; border-radius:6px; margin:0.5rem 0 0; color:#3A2A00 !important; }}
.cs .code {{ background:#F6F6F6; border:1px solid #E5E5E5; border-radius:6px; padding:0.6rem 0.8rem; font-family:Menlo,Consolas,monospace; font-size:0.82rem; color:#1A1A1A !important; margin:0.3rem 0 0.7rem; white-space:pre-wrap; }}
.cs .footer {{ background:{DARK}; color:#D9D9D9 !important; text-align:center; font-size:0.85rem; padding:0.8rem; border-radius:10px; margin-top:0.6rem; }}
@media (max-width:800px) {{ .cs .kpis, .cs .cards, .cs .cards.four {{ grid-template-columns:repeat(2,1fr); }} .cs .bricks {{ display:none; }} .cs .btitle {{ font-size:1.6rem; }} }}
"""

def dot(x, y, d, col, ring=False):
    st = f"border:5px solid {col};background:transparent;" if ring else f"background:{col};"
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;{st}"></div>'

def bar(x, y, w, h, col):
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{h//2}px;background:{col};"></div>'

BRICKS = '<div class="bricks">' + "".join([
    bar(10, 70, 120, 14, "#8E7CF0"), bar(60, 100, 150, 14, "#FFFFFF"), bar(150, 40, 120, 14, GREEN),
    dot(0, 20, 44, YEL), dot(120, 84, 46, "#FFFFFF", True), dot(222, 92, 56, YEL, True),
    dot(250, 0, 34, "#FFFFFF"), dot(96, 16, 26, GREEN),
]) + '</div>'

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in rows)
    return f'<table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'

def cards(items, cls=""):
    out = []
    for i, (t, b) in enumerate(items):
        col = TABCOL[(i + 2) % 4]
        out.append(f'<div class="card" style="border-top-color:{col};"><h4>{t}</h4><div>{b}</div></div>')
    return f'<div class="cards {cls}">' + "".join(out) + "</div>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def note(t):
    return f'<div class="note">{t}</div>'

def p(t):
    return f"<p>{t}</p>"


BANNER = (
    '<div class="banner">' + BRICKS +
    '<span class="tag">Prepared for Payward · Global Sourcing team</span>'
    '<div class="btitle">Sourcing at pace across tech, security and non-tech: a Payward execution plan</div>'
    '<div class="bsub">Three live-style searches run in parallel across Kraken and the wider Payward group, from hiring manager intake to a calibrated slate</div>'
    '<div class="by"><b>Adam Baig</b> · Sourcer · London (remote) · '
    '<a href="https://www.linkedin.com/in/adambaiguk">LinkedIn</a> · '
    '<a href="https://github.com/SkynetAI-Labs">GitHub</a> · '
    '<a href="https://gitlab.com/SkynetAI-Labs">GitLab</a></div>'
    '</div><div class="stripe"></div>'
)

KPIS = '<div class="kpis">' + "".join(
    f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in [
        ("3", "Searches in parallel: tech, security, non-tech"), ("5 days", "Target to first calibrated slate"),
        ("300+", "Profiles mapped across the three searches"), ("30%+", "Target outreach response rate")]
) + "</div>"

S = []

S.append(("Intake & hiring strategy", p(
    "<b>The scenario.</b> Payward is building one interoperable stack connecting crypto, tokenised assets and traditional markets, "
    "across Kraken, NinjaTrader, Reap and other businesses. This plan shows how I would run three different searches at once, "
    "with quick turnaround, as part of the Global Sourcing team. It is a hypothetical plan built on public information. No real candidates are named.")
 + table(["Search", "Business", "Type", "Why it is hard"], [
    ["Cloud Security Engineer (AWS / GCP)", "Kraken", "Security", "Small pool with real cloud security depth; every exchange and fintech wants them"],
    ["Senior Rust Engineer, trading systems", "Kraken", "Tech", "Rust plus low-latency or exchange experience is rare; most are not looking"],
    ["Compliance Analyst, AML / KYC", "Reap or NinjaTrader", "Non-tech", "Needs crypto and payments regulation knowledge across different regions"],
 ]) + cards([
    ("Intake with the hiring manager", ul(["Problem the hire solves in the first 6 months", "Must-haves vs trainable skills", "Payzone and time zone limits", "Where past great hires came from"])),
    ("Hiring strategy with the recruiter", ul(["Target company map and no-go list", "Sourcing lanes and weekly volume", "Screening questions agreed up front", "Close plan, including pay in crypto option"])),
    ("Calibration in 48 hours", ul(["Share 5 sample profiles per search", "Hiring manager rates yes, maybe, no", "Adjust strings and pools the same day", "Then build the full slate"])),
 ]) + note("Fast calibration is where speed comes from: a 48-hour check stops the team spending a week on the wrong profile.")))

S.append(("Market intelligence", p("Where the target talent sits, how easy it is to move, and what the hiring manager should know before we start.")
 + table(["Search", "Where the talent is", "Supply", "Competition"], [
    ["Cloud Security Engineer", "Crypto exchanges, fintechs and neobanks, cloud-native SaaS, security consultancies", "Tight", "Very high: every regulated fintech is hiring"],
    ["Senior Rust Engineer", "Trading firms, exchanges, blockchain infrastructure, systems and database companies", "Very tight", "Very high, with heavy equity offers"],
    ["Compliance Analyst", "Payments and card issuers, exchanges, crypto custodians, banks moving into digital assets", "Medium", "High in regulated hubs"],
 ]) + cards([
    ("Industry trends", ul(["Tokenised assets and stablecoin payments growing fast", "Regulation such as MiCA raising demand for compliance talent", "Security teams moving to cloud guardrails and automation"])),
    ("Location and payzones", ul(["Remote-first opens the global pool", "Payzones shape which markets to source first", "Time zone overlap matters for on-call and trading hours"])),
    ("What to tell the hiring manager", ul(["Rust plus trading experience may need a trade-off", "Security candidates often hold several offers", "Compliance talent is strongest in regulated hubs"])),
 ]) + note("I would share a one-page market snapshot per search after day 3, so hiring managers can make trade-offs early.")))

S.append(("Search 1: Cloud Security Engineer", p("<b>Security search.</b> Owning cloud security guardrails across AWS and GCP, supporting incident response, threat detection and compliance reviews.")
 + cards([
    ("Must-haves", ul(["AWS and/or GCP security controls in production", "IAM, logging and detection at scale", "Infrastructure as code (Terraform)", "Kubernetes and container security"])),
    ("Target pools", ul(["Exchanges and custodians", "Neobanks and payments companies", "Cloud-native SaaS security teams", "Security consultancies with cloud practices"])),
    ("Why I can calibrate this", ul(["Hands-on labs in AWS IAM, CloudTrail, CloudWatch detection and incident response", "Kubernetes hardening, Terraform and Checkov", "Can tell real depth from keyword CVs"])),
 ])
 + '<div class="code">("cloud security" OR "security engineer" OR "infrastructure security") AND (AWS OR GCP) AND (IAM OR CloudTrail OR GuardDuty OR "Security Command Center") AND (Terraform OR Kubernetes) AND (fintech OR crypto OR exchange OR payments)</div>'
 + '<div class="code">site:github.com (terraform OR checkov OR "aws-iam") security (policy OR guardrails) -tutorial</div>'
 + table(["Screening question", "What a strong answer shows"], [
    ["How would you stop a leaked access key being used?", "Detection, least privilege, automated response"],
    ["How do you add guardrails without slowing engineers?", "Policy as code, paved roads, clear exceptions"],
    ["Walk me through an incident you handled in the cloud", "Ownership, timeline, what changed afterwards"],
 ])))

S.append(("Search 2: Senior Rust Engineer", p("<b>Tech search.</b> Building low-latency, highly reliable trading and exchange systems in Rust.")
 + cards([
    ("Must-haves", ul(["Production Rust, not side projects only", "Concurrency and performance tuning", "Distributed systems at scale", "Bonus: trading, matching engines or blockchain"])),
    ("Target pools", ul(["Trading and market-making firms", "Exchanges and blockchain infrastructure", "Systems, database and networking companies", "Open-source Rust contributors"])),
    ("Lanes", ul(["GitHub X-ray on Rust repos", "Rust conference speakers and meetups", "Referrals from current engineers", "Silver medallists in the internal database"])),
 ])
 + '<div class="code">("Rust" OR "Rustlang") AND ("low latency" OR "high performance" OR "matching engine" OR "trading systems" OR tokio) AND (engineer OR developer) -intern -junior</div>'
 + '<div class="code">site:github.com "language:Rust" (tokio OR async OR "order book" OR "matching engine")</div>'
 + note("Open-source work is the best signal here. I would review commits and code quality before outreach and mention the specific project in the first message.")))

S.append(("Search 3: Compliance Analyst (non-tech)", p("<b>Non-tech search.</b> AML and KYC analyst supporting onboarding, transaction monitoring and regulatory reporting for a Payward business such as Reap or NinjaTrader.")
 + cards([
    ("Must-haves", ul(["AML, KYC and sanctions screening", "Transaction monitoring and case handling", "Crypto or payments regulation knowledge", "Clear written reporting"])),
    ("Target pools", ul(["Card issuers and payments companies", "Exchanges and crypto custodians", "Banks with digital-asset teams", "RegTech and compliance consultancies"])),
    ("Fintech knowledge I bring", ul(["Built a fraud detection and transaction-monitoring lab", "Know how exchanges, custody and stablecoin payments work", "Active crypto trader since 2021"])),
 ])
 + '<div class="code">("AML" OR "KYC" OR "financial crime" OR "transaction monitoring") AND (analyst OR specialist) AND (crypto OR "digital assets" OR payments OR stablecoin OR cards) AND (MiCA OR FATF OR "travel rule" OR sanctions)</div>'
 + note("For non-tech searches, regulation and region matter as much as title. The intake confirms which licences and markets the hire will cover.")))

S.append(("Outreach & candidate flow", cards([
    ("Channels", ul(["LinkedIn and Boolean search", "Internet and X-ray searches", "Social media and crypto communities", "Internal database and job boards", "Networking and referrals"])),
    ("Outreach", ul(["Personal first line tied to their work", "Why Payward, why now, in two lines", "Async-friendly: easy to reply when it suits them", "Two follow-ups with new information"])),
    ("Data I track weekly", ul(["Response rate by channel and message", "Pass-through rate at each stage", "Time from first contact to screen", "Where hires actually came from"])),
]) + table(["Stage", "Security", "Rust", "Compliance"], [
    ["Mapped", "110", "120", "80"], ["Contacted", "45", "50", "35"], ["Replied", "15", "14", "13"],
    ["Screened", "8", "7", "8"], ["Slate", "4", "3", "4"],
 ]) + note("If one channel stops working I change the message or the pool within days, not weeks, using the numbers above.")))

S.append(("Managing uncertainty", p("Payward often hires for roles nobody has filled before, with no data or track record. This is how I would approach a role I have never seen, such as a product lead for tokenised stocks.")
 + table(["When", "What I do"], [
    ["First 2 hours", "Read the product, public docs and filings; list the skills the role really needs"],
    ["Day 1", "Find 3 to 5 adjacent roles that share those skills, such as equities product, brokerage or tokenisation"],
    ["Day 2", "Build test strings, review 20 profiles with the hiring manager, agree the real must-haves"],
    ["Day 3 to 5", "Full sourcing across the agreed pools, with a short market note on what we found"],
 ]) + p("<b>A market I have never recruited in.</b> The same approach works when the role is familiar but the market is new.")
 + table(["When", "What I do"], [
    ["First 4 hours", "Find who employs this talent locally: competitors, big local employers and fast-growing companies"],
    ["Day 1", "Learn the basics: pay levels, notice periods, right to work, local job boards, communities and language needs"],
    ["Day 1", "Talk to people on the ground: in-country colleagues, recent hires and local hiring managers"],
    ["Day 2", "Build and test local strings, review first profiles with the hiring manager and agree what good looks like there"],
 ]) + note("Scrappiness means treating a role with no playbook as an opportunity to build the first one for the team.")))

S.append(("Team, tools & research project", cards([
    ("Sharing with the team", ul(["Shared library of tested Boolean strings by role", "Market maps saved for reuse", "Short notes on what worked each week"])),
    ("Research project", ul(["Rediscover strong past candidates in the internal database", "Tag them by skill, payzone and interest", "Re-engage them for new roles before external sourcing"])),
    ("Tools", ul(["LinkedIn Recruiter and Insights", "Greenhouse or Ashby", "Claude and Gemini for research, always checked", "Streamlit dashboards for funnel data"])),
]) + note("No solo players: every string, map and insight I build goes into a shared space the whole sourcing team can use.")))

S.append(("Ambassador & candidate experience", cards([
    ("Sharing Payward's values", "Talk honestly about the mission, remote-first culture and crypto ethos, and expect candidates to try the Kraken app"),
    ("Brand awareness", "Show up in crypto, security and Rust communities so people know the name before we message them"),
    ("Respect for candidates", "Clear timelines, fast replies and honest feedback, even for people we do not move forward"),
])))

S.append(("First 30 days & KPIs", table(["Week", "Focus", "Output"], [
    ["1", "Learn the businesses, payzones, tools and team playbooks", "Intake notes and calibration on first roles"],
    ["2", "Run live searches across tech, security and non-tech", "First calibrated slates"],
    ["3", "Build market maps and share strings with the team", "Market snapshots for hiring managers"],
    ["4", "Start the research project on internal rediscovery", "First re-engaged candidates and a short report"],
 ]) + cards([
    ("Time to first slate", "5 working days"),
    ("Response rate", "30%+"),
    ("Slate to interview", "50%+"),
    ("Hiring manager rating", "4.5 / 5"),
], "four")))

S.append(("How I would work", cards([
    ("Sourcing track record", "15 years of sourcing and headhunting; around 70% of 120+ GTM hires came from my own outbound sourcing, with around a 90% offer-accept rate"),
    ("Security and cloud skills", "Google cybersecurity and Google Cloud certificates, plus 16 published labs across AWS, Kubernetes, DevSecOps and incident response"),
    ("Crypto and fintech", "Active crypto trader since 2021; designed C.I.P.H.E.R., a crypto market-intelligence system; built a fintech case study with fraud and transaction monitoring"),
    ("Builder mentality", "Built PeachBox., an AI recruiting platform, and live hiring dashboards; I like improving how hiring works, not just running searches"),
], "two") + note("High agency, bias for action and team first: fast, scrappy and careful with quality.")))

def nav():
    out = []
    for i, (t, _) in enumerate(S):
        col = TABCOL[i % 4]
        fg = "#3A2A00" if col == YEL else "#FFFFFF"
        out.append(f'<a href="#s{i+1}" style="background:{col};color:{fg} !important;">{i+1:02d} {t}</a>')
    return '<div class="nav">' + "".join(out) + "</div>"

def block(i):
    t, body = S[i]
    col = TABCOL[i % 4]
    fg = "#3A2A00" if col == YEL else "#FFFFFF"
    return (f'<div class="block" id="s{i+1}"><div class="bh" style="background:{col};color:{fg} !important;">'
            f'<small>SECTION {i+1:02d}</small>{t}</div><div class="bb">{body}</div></div>')

FOOTER = '<div class="footer">Prepared by Adam Baig · London, UK · A hypothetical sourcing plan built on public information. No real candidates named.</div>'

def full_html():
    return BANNER + KPIS + nav() + "".join(block(i) for i in range(len(S))) + FOOTER
