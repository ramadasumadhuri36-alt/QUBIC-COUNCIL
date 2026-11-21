import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_COLOR = RGBColor(15, 23, 42)       # #0f172a (Navy Slate)
    CARD_BG = RGBColor(30, 41, 59)        # #1e293b
    ACCENT_CYAN = RGBColor(56, 189, 248)  # #38bdf8
    ACCENT_INDIGO = RGBColor(129, 140, 248) # #818cf8
    TEXT_LIGHT = RGBColor(248, 250, 252)  # #f8fafc
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94a3b8

    def apply_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    slides_data = [
        {
            "tag": "EXECUTIVE OVERVIEW",
            "title": "Qubic Council: The Multi-LLM Consensus Engine",
            "subtitle": "Harnessing Collective AI Intelligence & Autonomous Cross-Model Peer Review",
            "points": [
                ("Orchestrated Multi-LLM Execution", "Queries 1 to 4 frontier models (OpenAI, Claude, Gemini, Groq) simultaneously rather than relying on a single fallible model."),
                ("Autonomous Peer Review Mechanism", "Models critically evaluate, critique, and grade each other's outputs to filter out hallucinations."),
                ("Consensus Synthesis Pipeline", "Clusters verified claims and computes confidence scores to produce an authoritative synthesized response.")
            ]
        },
        {
            "tag": "THE CORE PROBLEM",
            "title": "The Blind Spots of Single-Model AI",
            "subtitle": "Why high-stakes operations cannot rely on a single LLM response",
            "points": [
                ("Confident Hallucinations", "A single AI can generate convincingly flawed, ungrounded answers without self-awareness or internal checks."),
                ("Provider Bias & Blind Spots", "Every foundational model carries training biases, domain weaknesses, and uneven reasoning capabilities."),
                ("Zero Verification Traceability", "Traditional chatbots provide answers as a 'black box' with no verifiable reasoning trail or peer validation.")
            ]
        },
        {
            "tag": "THE SOLUTION",
            "title": "Collective Intelligence & Peer Review",
            "subtitle": "Democracy and rigorous peer-review applied to artificial intelligence",
            "points": [
                ("Dynamic Council Architecture", "Configure 1 to 4 models dynamically based on task importance and query complexity."),
                ("Adversarial Peer Review", "Cross-model validation where AI models audit counter-claims before final acceptance."),
                ("Cryptographic Context Locking", "Normalized prompts are hashed to guarantee that every model answers under identical strict constraints.")
            ]
        },
        {
            "tag": "SYSTEM ARCHITECTURE",
            "title": "The 8-Layer Consensus Pipeline",
            "subtitle": "End-to-end flow from raw prompt to synthesized truth",
            "points": [
                ("Layers 1-3: Setup & Execution", "Normalization (intent/domain detection) -> Constraint Locking (hash guarantee) -> Parallel Model Execution."),
                ("Layers 4-5: Extraction & Peer Audit", "Atomic Claim Extraction deconstructs outputs -> Cross-Model Peer Review scores and challenges claims."),
                ("Layers 6-8: Scoring & Synthesis", "Agreement Clustering (semantic grouping) -> Scored Consensus -> Final Synthesized Master Response.")
            ]
        },
        {
            "tag": "DEEP DIVE",
            "title": "Cross-Model Peer Review & Agreement Engine",
            "subtitle": "How conflicting opinions turn into high-confidence consensus",
            "points": [
                ("Atomic Claim Decomposition", "Every model's raw output is dissected into distinct, testable, atomic factual statements."),
                ("Matrix Peer Scoring", "Each model reviews peer claims with thumbs up/down, critique notes, and confidence deductions."),
                ("Semantic Cluster Weighting", "Natural Language embeddings group matching claims, applying mathematical weights based on agreement ratio.")
            ]
        },
        {
            "tag": "USER EXPERIENCE",
            "title": "Live Interactive Visualizer Dashboard",
            "subtitle": "Total transparency and control in real time",
            "points": [
                ("Universal API Key Auto-Detection", "Paste one key (OpenRouter, OpenAI, Groq) and the engine automatically configures available models."),
                ("Real-Time Consensus Graph", "Interactive UI displaying stage-by-stage status, claim clusters, and model debate cards."),
                ("Persistent Conversation History", "Save, inspect, and reload audit trails of past decisions with full consensus metrics.")
            ]
        },
        {
            "tag": "ENGINEERING",
            "title": "High-Performance Tech Stack",
            "subtitle": "Modern, asynchronous, and scalable infrastructure",
            "points": [
                ("Backend Engine", "Python 3.10+, FastAPI, and AsyncIO for lightning-fast concurrent model execution."),
                ("Intelligence & Algorithms", "Scikit-Learn & NetworkX for semantic clustering and graph traversal; OpenAI/OpenRouter SDKs."),
                ("Frontend & Interface", "Zero-friction TailwindCSS and Vanilla JS client with responsive live-updating visualizers.")
            ]
        },
        {
            "tag": "BUSINESS VALUE",
            "title": "Use Cases & Future Horizons",
            "subtitle": "Where verifiable AI consensus is mission-critical",
            "points": [
                ("High-Stakes Decision Making", "Legal document analysis, medical/scientific research synthesis, and algorithmic risk audits."),
                ("Automated Code & Architecture Review", "Multi-model cross-auditing for security vulnerabilities, logic flaws, and performance bottlenecks."),
                ("Next Milestones", "Decentralized model consensus, multi-modal verification (images & documents), and automated external fact-checking.")
            ]
        }
    ]

    for data in slides_data:
        slide = prs.slides.add_slide(blank_layout)
        apply_background(slide)

        # Header Container
        header_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.6), Inches(11.3), Inches(1.8))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = data["tag"].upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_CYAN
        p_tag.space_after = Pt(4)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = data["title"]
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT
        p_title.space_after = Pt(6)

        # Subtitle
        p_sub = tf.add_paragraph()
        p_sub.text = data["subtitle"]
        p_sub.font.size = Pt(14)
        p_sub.font.color.rgb = TEXT_MUTED

        # 3 Structured Cards for Points
        card_width = Inches(3.6)
        card_height = Inches(4.2)
        card_top = Inches(2.5)
        gap = Inches(0.25)
        start_left = Inches(1.0)

        for i, (point_title, point_desc) in enumerate(data["points"]):
            left = start_left + i * (card_width + gap)
            
            # Card Shape
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, card_top, card_width, card_height)
            card.fill.solid()
            card.fill.fore_color.rgb = CARD_BG
            card.line.color.rgb = RGBColor(51, 65, 85) # slate-700
            card.line.width = Pt(1)

            # Card Content
            c_box = slide.shapes.add_textbox(left + Inches(0.25), card_top + Inches(0.35), card_width - Inches(0.5), card_height - Inches(0.7))
            ctf = c_box.text_frame
            ctf.word_wrap = True
            ctf.margin_left = ctf.margin_top = ctf.margin_right = ctf.margin_bottom = 0

            # Step / Card Number
            p_num = ctf.paragraphs[0]
            p_num.text = f"0{i+1}"
            p_num.font.size = Pt(12)
            p_num.font.bold = True
            p_num.font.color.rgb = ACCENT_INDIGO
            p_num.space_after = Pt(8)

            # Point Title
            p_pt = ctf.add_paragraph()
            p_pt.text = point_title
            p_pt.font.size = Pt(17)
            p_pt.font.bold = True
            p_pt.font.color.rgb = TEXT_LIGHT
            p_pt.space_after = Pt(12)

            # Point Description
            p_pd = ctf.add_paragraph()
            p_pd.text = point_desc
            p_pd.font.size = Pt(13)
            p_pd.font.color.rgb = TEXT_MUTED

    output_path = "Qubic_Council_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation generated successfully: {output_path}")

if __name__ == "__main__":
    create_deck()
