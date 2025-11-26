import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from emotion_model import EmotionalAnalyzer
import time

# Page configuration
st.set_page_config(
    page_title="AI Emotional Journal",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with better loading states
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .emotion-card {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 0.5rem 0;
    }
    .suggestion-card {
        padding: 1rem;
        border-radius: 10px;
        background-color: #e8f4fd;
        margin: 0.5rem 0;
        border-left: 4px solid #1f77b4;
    }
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .loading-spinner {
        text-align: center;
        padding: 2rem;
    }
    .fallback-warning {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .example-button {
        width: 100%;
        margin: 0.2rem 0;
        text-align: left;
        white-space: normal;
        height: auto;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_analyzer():
    """Load the emotional analyzer model with better error handling"""
    try:
        with st.spinner("🔄 Loading AI models... This may take a minute."):
            analyzer = EmotionalAnalyzer()
            return analyzer
    except Exception as e:
        st.error(f"Error loading analyzer: {e}")
        return None


def display_emotional_analysis(emotion_data, context):
    """Display emotional analysis results"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Primary Emotion",
            value=emotion_data['primary_emotion'].title(),
            delta=f"{emotion_data['primary_score']:.1%} confidence"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Emotional Intensity",
            value=f"{emotion_data['emotional_intensity']:.1%}",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Overall Sentiment",
            value=context['sentiment'],
            delta=f"{context['intensity']:.1%} intensity"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Emotion distribution
    st.subheader("Emotion Distribution")
    emotions_df = pd.DataFrame([
        {'Emotion': emotion, 'Score': score}
        for emotion, score in emotion_data['all_emotions'].items()
    ])

    fig = px.bar(
        emotions_df,
        x='Emotion',
        y='Score',
        color='Score',
        color_continuous_scale='Blues',
        title="Emotional Profile Distribution"
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def display_context_analysis(context):
    """Display context analysis results"""
    st.subheader("📋 Extracted Context")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Detected Topics:**")
        if context['topics']:
            for topic in context['topics']:
                st.markdown(f"- {topic}")
        else:
            st.write("No specific topics detected")

        st.markdown("**Key Entities/People:**")
        if context['key_entities']:
            for entity in context['key_entities']:
                st.markdown(f"- {entity}")
        else:
            st.write("No specific entities detected")

    with col2:
        st.markdown("**Sentiment Analysis:**")
        sentiment_emoji = "😊" if context['sentiment'] == 'POSITIVE' else "😔" if context[
                                                                                    'sentiment'] == 'NEGATIVE' else "😐"
        st.markdown(f"Sentiment: {sentiment_emoji} {context['sentiment']}")
        st.markdown(f"Intensity: {context['intensity']:.1%}")

        # Sentiment gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=context['intensity'] * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Sentiment Strength"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 33], 'color': "lightgray"},
                    {'range': [33, 66], 'color': "gray"},
                    {'range': [66, 100], 'color': "darkgray"}
                ],
            }
        ))
        st.plotly_chart(fig, use_container_width=True)


def display_suggestions(suggestions):
    """Display personalized suggestions"""
    st.subheader("💡 Personalized Suggestions")

    for i, suggestion in enumerate(suggestions, 1):
        st.markdown(f'<div class="suggestion-card">'
                    f'<strong>Suggestion {i}:</strong> {suggestion}'
                    f'</div>', unsafe_allow_html=True)

    # Additional resources
    st.markdown("---")
    st.subheader("Additional Resources")

    resource_cols = st.columns(2)
    with resource_cols[0]:
        st.info("**Mindfulness Apps:**\n- Headspace\n- Calm\n- Insight Timer")
    with resource_cols[1]:
        st.info(
            "**Crisis Support:**\n- National Suicide Prevention Lifeline: 988\n- Crisis Text Line: Text HOME to 741741")


def display_visualizations(emotion_data, context):
    """Display emotional visualizations"""
    st.subheader("📈 Emotional Visualization")

    # Create radar chart for emotions
    emotions = list(emotion_data['all_emotions'].keys())
    scores = list(emotion_data['all_emotions'].values())

    # Ensure we have at least 3 emotions for radar chart
    if len(emotions) >= 3:
        fig = go.Figure(data=go.Scatterpolar(
            r=scores + [scores[0]],  # Close the radar
            theta=emotions + [emotions[0]],  # Close the radar
            fill='toself',
            name='Emotional Profile'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=False,
            title="Emotional Profile Radar Chart"
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Not enough emotion data for radar chart visualization")


def main():
    # Header
    st.markdown('<h1 class="main-header">🧠 AI Emotional Journal</h1>', unsafe_allow_html=True)
    st.markdown("### Understand your emotions and get personalized suggestions")

    # Sidebar
    st.sidebar.title("About")
    st.sidebar.info(
        "This AI Emotional General analyzes your text to understand emotions and context, "
        "providing personalized suggestions for emotional well-being."
    )

    st.sidebar.title("How to Use")
    st.sidebar.write("""
    1. Enter your thoughts or feelings in the text area
    2. Click 'Analyze Emotions'
    3. View detailed emotional analysis
    4. Get personalized suggestions
    """)

    # Initialize analyzer
    if 'analyzer' not in st.session_state:
        analyzer = load_analyzer()
        if analyzer is None:
            st.error("❌ Failed to load AI models. Please refresh the page.")
            return
        st.session_state.analyzer = analyzer

    analyzer = st.session_state.analyzer

    # Show fallback warning if using fallback mode
    if not analyzer.models_loaded:
        st.markdown('<div class="fallback-warning">', unsafe_allow_html=True)
        st.warning("⚠️ Using fallback analysis mode. Some advanced features may be limited.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Initialize session state for text input
    if 'user_text' not in st.session_state:
        st.session_state.user_text = ""

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Share Your Thoughts")

        # Text area that uses session state
        user_text = st.text_area(
            "Enter your text here:",
            height=150,
            placeholder="Type your thoughts, feelings, or experiences here...\nExample: 'I felt really anxious about my presentation tomorrow. I keep thinking about what could go wrong.'",
            value=st.session_state.user_text,
            key="text_input"
        )

        # Update session state when text changes
        if user_text != st.session_state.user_text:
            st.session_state.user_text = user_text

        analyze_button = st.button("🧠 Analyze Emotions", type="primary", use_container_width=True)

    with col2:
        st.subheader("Example Inputs")
        examples = [
            "I'm so excited about my vacation next week! I can't wait to relax on the beach.",
            "I'm really frustrated with my team at work. They never listen to my ideas.",
            "I feel lonely and isolated lately. I miss spending time with my friends.",
            "The news about climate change makes me worried about the future.",
            "I accomplished all my goals today and feel incredibly proud of myself!"
        ]

        # Create example buttons that update session state
        for i, example in enumerate(examples):
            if st.button(
                    example[:60] + "..." if len(example) > 60 else example,
                    key=f"example_{i}",
                    use_container_width=True,
                    type="secondary"
            ):
                st.session_state.user_text = example
                

    # Handle analysis
    if analyze_button and st.session_state.user_text.strip():
        with st.spinner("🔍 Analyzing your emotions..."):
            # Add small delay for better UX
            time.sleep(0.5)

            try:
                # Analyze emotions and context
                emotion_data = analyzer.analyze_emotion(st.session_state.user_text)
                context = analyzer.extract_context(st.session_state.user_text)
                suggestions = analyzer.get_suggestions(emotion_data, context)

                st.success("✅ Analysis Complete!")

                # Display model status
                if not analyzer.models_loaded:
                    st.info("ℹ️ Analysis performed using fallback methods")

                # Create tabs for different views
                tab1, tab2, tab3, tab4 = st.tabs(
                    ["📊 Emotional Analysis", "🎯 Context", "💡 Suggestions", "📈 Visualization"])

                with tab1:
                    display_emotional_analysis(emotion_data, context)

                with tab2:
                    display_context_analysis(context)

                with tab3:
                    display_suggestions(suggestions)

                with tab4:
                    display_visualizations(emotion_data, context)

            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("Please try again with different text.")

    elif analyze_button and not st.session_state.user_text.strip():
        st.warning("⚠️ Please enter some text to analyze.")


if __name__ == "__main__":
    main()


