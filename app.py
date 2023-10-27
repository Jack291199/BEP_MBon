import streamlit as st
import requests
from PIL import Image
from streamlit_option_menu import option_menu
import threading

def set_up():
    st.set_page_config(page_title=None, page_icon=None, layout="wide")

    custom_style = """
    <style>
        .stApp {
            background-color: #ECDFBE;
        }
    </style>
    """

    st.markdown(custom_style, unsafe_allow_html=True)





selected = option_menu(
    menu_title=None,
    options=["GIỚI THIỆU", "MÂM XÔI", "MENU","LIÊN HỆ"],
    icons=["house", "book", "book","telephone"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",)



#------TẤT CẢ ẢNH-----
chungchi = Image.open("image/gt.chungchi.png")
chungchi = chungchi.resize((480, 400))

lambanh = Image.open("image/gt.lambanh.png")
lambanh = lambanh.resize((480, 400))

mam_do = Image.open("image/mam_do.png")
mam_do = mam_do.resize((600, 600))

mam_vang = Image.open("image/mam_vang.png")
mam_vang = mam_vang.resize((600, 600))

mam_xanh = Image.open("image/mam_xanh.png")
mam_xanh = mam_xanh.resize((600, 600))

mam_xanh2 = Image.open("image/mam_xanh2.png")
mam_xanh2 = mam_xanh2.resize((600, 600))

mam_hong = Image.open("image/mam_hong.png")
mam_hong = mam_hong.resize((600, 600))



menu1 = Image.open("image/menu1.png")
menu1 = menu1.resize((700, 800))


menu2 = Image.open("image/menu2.png")
menu2 = menu2.resize((700, 800))

menu3 = Image.open("image/menu3.png")
menu3 = menu3.resize((700, 800))

menu4 = Image.open("image/menu4.png")
menu4 = menu4.resize((700, 800))






def text_intro():
    # header
    with st.container():
        st.title("BẾP MBon XIN CHÀO QUÝ KHÁCH")

    with st.container():
        st.write("----")
        left_column, right_column = st.columns((2, 1))
        with left_column:
            st.header("Trần Thị Quyên")
            st.write("##")
            st.write(
                "Xin chào ba mẹ các bé, tớ là Quyên. Xuất phát điểm là giao viên mầm non, tớ có một tình yêu, sự gắn kết rất đặc biệt với các bạn nhỏ."
                "Chính vì vậy để giành tặng những thiên thần nhỏ bé của những món quà ý nghĩa và thực tế nhất, tớ đã giành ra rất nhiều thời gian học hỏi"
                " và rèn luyện. Tớ đã có 5 năm kinh nghiệm để làm ra những mâm xôi đầy tháng, những bát thạch đẹp mắt để đáp ứng nhu cầu của các ba mẹ."
                " Đã có hàng ngàn mâm đầy tháng được được các vị khách yêu quý lựa chọn và giành những lời khen. Mời các bạn cùng xem những hình Ảnh"
                "Quyên cùng các khóa học làm xôi , thạch từ các chuyên gia hàng đầu trong ngành nhé"
                )

            st.markdown("[Facebook của Quyên](https://www.facebook.com/quyen.mituot.5?mibextid=LQQJ4d)")
def pic_intro1():
    # --------ẢNH GIỚI THIỆU-----
    with st.container():
        st.write("----")
        st.header("Hình ảnh thực tế của Quyên ")
        image_column, text_column = st.columns((1, 2))

        with image_column:
            st.image(chungchi)

        with text_column:
            st.header("TOP 3 gian hàn xuất sắc nhất tỉnh Quảng Ninh!")
            st.write("Ẩm Thực Quảng Ninh là ngày hội ẩm thực cực kì lớn và chuyên nghiệp thu hút hàng chục ngàn du khách trong và ngoài nước "
                     " với 200 gian hàng  được lựa chọn kĩ càng và khắt khe từ khắp nơi trên mọi miền tổ quốc. Gian hàng của Quyên đã "
                     "đạt top 3 gian hàng xuất sắc nhất của hội chợ. Một minh chứng thuyết phục nhất về chất lương cũng như uy tín của"
                     " BẾP MBon")

            st.markdown("[Ẩm Thực Quảng Ninh](https://danviet.vn/khai-mac-lien-hoan-am-thuc-quang-ninh-nam-2023-20230729005512948.htm)")
def pic_intro2():
    # ---------------------------
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(lambanh)
        with text_column:
            st.header("BẾP MBon có số lượng khách lớn nhất Quảng Yên")
            st.write("Đối với Quyên thì sự chỉnh chu, chất lượng và uy tín là 3 tiêu chí hàng đầu trong quá trình làm mâm đầy tháng."
                     "Mỗi sản phẩm Quyên làm là sự tâm huyết cũng như tình cảm giành cho các bạn nhỏ . 5 năm qua , đã có hàng nghìn đơn"
                     " hàng của các ba mẹ. Quyên xin cảm ơn sự tin tưởng, ủng hộ của tất cả mọi người")
            st.markdown("[Các hình ảnh khác ](https://www.facebook.com/quyen.mituot.5?mibextid=LQQJ4d)")
def address_intro():
    # ---- Địa chỉ ----
    with st.container():
        st.write("---")
        st.header("Địa chỉ")
        st.write("Hải Quyên Mobile - Ngã ba chợ Rộc - TX Quảng Yên - Quảng Ninh")
        st.write("SĐT: 0333 231 618")
        st.markdown("[Facebook: Trần Thị Quyên](https://www.facebook.com/quyen.mituot.5?mibextid=LQQJ4d)")




a = threading.Thread(target=text_intro,args=())
b = threading.Thread(target=pic_intro1,args=())
c = threading.Thread(target=pic_intro2,args=())
d = threading.Thread(target=address_intro,args=())

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()



#--------------MAM XOI----------------------------------------------------------------------------------------

#--mam do---
def mamdo():
    with st.container():

        text_column,image_column = st.columns((1, 2))
        with image_column:
            st.title("MÂM XÔI ĐỎ")
            st.image(mam_do)




    #--mam xanh----
def mamxanh():
    with st.container():

        text_column, image_column = st.columns((1, 2))
        with image_column:
            st.title("MÂM XÔI XANH")
            st.image(mam_xanh)

    #--mam xoi vang----
def mamvang():
    with st.container():

        text_column, image_column = st.columns((1, 2))
        with image_column:
            st.title("MÂM XÔI VÀNG")
            st.image(mam_vang)

    #----mam hong----

def mamhong():
    with st.container():
        text_column, image_column = st.columns((1, 2))
        with image_column:
            st.title("MÂM XÔI HỒNG")
            st.image(mam_hong)


a = threading.Thread(target=mamdo, args=())
b = threading.Thread(target=mamxanh, args=())
c = threading.Thread(target=mamvang, args=())
d = threading.Thread(target=mamhong, args=())

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()





#-----------------------MENU-------------------------------------------------------



#-----MAM 1----

def mam1():
    with st.container():

        text_column,image_column = st.columns((1, 2))
        with image_column:
            st.image(menu1)
        with text_column:
            st.write("#")



#----MAm 2-----
def mam2():
    with st.container():
        text_column,image_column = st.columns((1, 2))
        with image_column:
            st.image(menu2)
        with text_column:
            st.write("#")



#---MAM 3--
def mam3():
    with st.container():
        text_column,image_column = st.columns((1, 2))
        with image_column:
            st.image(menu3)
        with text_column:
            st.write("#")
#---MAM 4---
def mam4():
    with st.container():
        text_column,image_column = st.columns((1, 2))
        with image_column:
            st.image(menu4)
        with text_column:
            st.write("#")



a = threading.Thread(target=mam1, args=())
b = threading.Thread(target=mam2, args=())
c = threading.Thread(target=mam3, args=())
d = threading.Thread(target=mam4, args=())

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()



#-----------------CHAY MUTIL THREDING----------------------------
if selected == "GIỚI THIỆU":
    text_intro()
    pic_intro1()
    pic_intro2()
    address_intro()

elif selected == "MÂM XÔI":
    mamdo()
    mamxanh()
    mamvang()
    mamhong()
elif selected == "MENU":
    mam1()
    mam2()
    mam3()
    mam4()





#------------------------LIÊN HỆ---------------------------------------------------------
elif selected == "LIÊN HỆ":
    with st.container():
        text_column1, text_column2 = st.columns((1, 2))
        with text_column1:
            st.write("#")
        with text_column2:
            st.write("---")
            st.header("Địa chỉ")
            st.write("Hải Quyên Mobile - Ngã ba chợ Rộc - TX Quảng Yên - Quảng Ninh")
            st.write("SĐT: 0333 231 618")
            st.markdown("[Facebook: Trần Thị Quyên](https://www.facebook.com/quyen.mituot.5?mibextid=LQQJ4d)")

