import streamlit as st

st.header("🧠GROWTH MINDSET CHALLENGE🧠")
st.header(" 🚀Welcome To Your Journey🎊")
st.header("Unlock Your Potential with Daily Growth Challenges!")
st.subheader("Small Steps, Big Changes – Build a Growth Mindset One Challenge at a Time 🗽.")
st.write(" 🌱join the challenge...")
email=st.text_input("enter your email")
if st.button("JOIN NOW"): 
    if email: st.success(f"🎉 Welcome! Your first challenge will be sent to {email} soon.")
else: st.warning("Please enter a valid email address.")


st.header("🫵 What's Your Today Challenge?")
user=st.text_input(" 💪Describe a challange you are facing?")
if user:
     st.success(f"you are facing{user} 🌟 Keep pushing forward! Every challenge brings you closer to a growth mindset.")
else:
     st.warning("Tell us about your challenge to get started...")
     
st.header("The Failure Reframe 🎯")
st.text_input("Write about a recent failure and list three things you learned from it.")

st.header("Celebrate Your Achivements 🏆")
achive= st.text_input("Share something you have recently accomplished...")
if achive:
    st.success(f" 🤩Amazing your achivement {achive}")
else:
    st.warning("Small Steps, Big Changes – Build Resilience & Confidence👍")

def quiz(ans):
    return sum(ans)
st.title("🧠 Growth Mindset Quiz")
st.write("Find out your growth mindset level! Answer these questions honestly.")
questions=[
      ("1️⃣ When faced with a challenge, do you:", ["Avoid it", "Try but give up quickly", "Embrace it and learn"]),
    ("2️⃣ When you fail, do you:", ["Feel like a failure", "Blame circumstances", "See it as a lesson"]),
    ("3️⃣ How do you see effort?", ["Useless", "Sometimes helpful", "Essential for success"]),
    ("4️⃣ When receiving feedback, do you:", ["Ignore it", "Take it personally", "Use it to improve"]),
    ("5️⃣ How do you feel about others’ success?", ["Jealous", "Indifferent", "Inspired"])
]
ans=[]
for questions,options in questions:
    choice=st.radio(questions, options, index=1) 
    ans.append(options.index(choice))
     
if st.button("Get My Result"):
    score=quiz(ans)
    if score <=5:
        if score <= 5:st.error("🔴 Fixed Mindset: You see abilities as unchangeable. Try stepping out of your comfort zone!")
        st.write("💡 **Challenge:** Try something new and embrace failure as a learning tool.")
    elif score <= 10:
        st.warning("🟠 Mixed Mindset: You're in between! Sometimes you persist, sometimes you hesitate.")
        st.write("💡 **Challenge:** Reframe negative thoughts and focus on progress.")
    else:
        st.success("🟢 Growth Mindset: You embrace challenges and see failure as an opportunity to grow!")
        st.write("💡 **Challenge:** Teach someone else a skill you recently learned.")


















st.write("---")
st.write("### 📊 Track Your Progress")
progress = st.slider("How many challenges have you completed?", 0, 30, 5)
st.progress(progress / 30)

st.write("🌟 Keep pushing forward! Every challenge brings you closer to a growth mindset.")
