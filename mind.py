import streamlit as st

st.title("Streamlit: The Best Way to Build Python Apps?")
st.write("""
Welcome! 🚀  
Streamlit makes it incredibly easy to turn Python scripts into web apps.
""")

st.header("Why Streamlit?")
st.markdown("""
- Super easy to set up
- Real-time updates
- Perfect for machine learning and data apps
""")

st.subheader("Comparison with Other Frameworks")
frameworks = ["Streamlit", "Dash", "Gradio"]
speed = [90, 70, 80]

st.bar_chart({"Frameworks": frameworks, "Ease of Use": speed})

st.success("Start building today!")