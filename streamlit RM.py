import streamlit as st
st.set_page_config(
    page_title="菅鑫语天天开心",
    page_icon="❤",
    #布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#一级标题设置
st.title("菅鑫语欢迎你呀！")
#文字段落设置
st.write("菅鑫语是世界上最漂亮，最体贴温柔的女人，她非常可爱善良")
st.write("菅鑫语喜欢吃水果，喜欢吃千层蛋糕。")
st.write("菅鑫语喜欢穿，喜欢画美美的妆")
st.write("菅鑫语喜欢小猫小狗")
#图片设置
st.image("./2.jpg",width=300)
#音频接受文段
st.write("菅鑫语生日的时候给我录制的时光机")
st.audio("./菅大美女的时光机.m4a")
#视频设置
st.write("给你买的平板你当时收得到老高兴了，还是有点歪哈哈哈，结果是摄像头的原因，我们俩好呆啊哈哈哈哈")
st.video("./平板.mp4")
st.write("发你视频的第一个朋友圈好可爱啊")
st.video("./菅大美女.mp4",width=300)
#logo
st.logo("./2.jpg")
#table
jian_date={
    "name":["菅鑫语","高航宇"],
    "age":[19,20],
    "sex":["女","男"]
}
st.table(jian_date)
#输入框
st_name = st.text_input("请输入你的名字")
st.write(f"你好呀，{st_name}")

password = st.text_input("请输入你的密码",type="password")
st.write(f"你好呀，{st_name}")
st.write(f"你的密码是，{password}")
#单选按钮
gender = st.radio("请选择你的性别",("男","女"),index=1)
st.write(f"你好呀，{st_name}")
st.write(f"你的性别是，{gender}")
#多选按钮
# ... existing code ...
#多选按钮
hobby = st.multiselect("请选择你的爱好",("唱歌","跳舞","画画","写代码"),default=["唱歌","画画"])
st.write(f"你好呀，{st_name}")
st.write(f"你的爱好是，{hobby}")
# ... existing code ...
