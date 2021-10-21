from flask import Flask, render_template, url_for


app = Flask(__name__)

import crawling

from selenium import webdriver


from bs4 import BeautifulSoup

#index

@app.route('/')
def hello():
    myList, myList_href = crawling.daum()
    today, today_href = crawling.today()
    clien, clien_href = crawling.clien()
    blog, blog_href = crawling.blog()
    blog1, blog1_href = crawling.blog1()
    blog2, blog2_href = crawling.blog2()
    blog3, blog3_href = crawling.blog3()
    blog4, blog4_href = crawling.blog4()
    blog5, blog5_href = crawling.blog5()
    blog6, blog6_href = crawling.blog6()
    blog7, blog7_href = crawling.blog7()
    blog8, blog8_href = crawling.blog8()
    blog9, blog9_href = crawling.blog9()
    blog10, blog10_href = crawling.blog10()
    blog11, blog11_href = crawling.blog11()



    return render_template("index.html",
                           list=myList, list_href=myList_href, list_len=len(myList),
                           list2=today, list2_href=today_href, list2_len=len(today),
                           list3=clien, list3_href=clien_href, list3_len=len(clien),
                           list4=blog, list4_href=blog_href, list4_len=len(blog),
                           list5=blog1, list5_href=blog1_href, list5_len=len(blog1),
                           list6=blog2, list6_href=blog2_href, list6_len=len(blog2),
                           list7=blog3, list7_href=blog3_href, list7_len=len(blog3),
                           list8=blog4, list8_href=blog4_href, list8_len=len(blog4),
                           list9=blog5, list9_href=blog5_href, list9_len=len(blog5),

                           list10=blog6, list10_href=blog6_href, list10_len=len(blog6),
                           list11=blog7, list11_href=blog7_href, list11_len=len(blog7),
                           list12=blog8, list12_href=blog8_href, list12_len=len(blog8),
                           list13=blog9, list13_href=blog9_href, list13_len=len(blog9),
                           list14=blog10, list14_href=blog10_href, list14_len=len(blog10),
                           list15=blog11, list15_href=blog11_href, list15_len=len(blog11)

                           )
#index1

@app.route('/about')
def about():


    list_daum, list_daum_href = crawling.daum()
    list_today, list_today_href = crawling.today()
    list_clien, list_clien_href = crawling.clien()



    return render_template("index1.html",
                           daum = list_daum,
                           today = list_today,
                           clien = list_clien,
                           daum_href = list_daum_href,
                           daum_len = len(list_daum),
                           today_len= len(list_today),
                           today_href = list_today_href,
                            clien_href = list_clien_href,
                            clien_len = len(list_clien),
                                        )


@app.route('/mobile')
def mobile():
    myList, myList_href = crawling.daum()
    today, today_href = crawling.today()
    clien, clien_href = crawling.clien()
    blog, blog_href = crawling.blog()
    blog1, blog1_href = crawling.blog1()
    blog2, blog2_href = crawling.blog2()
    blog3, blog3_href = crawling.blog3()
    blog4, blog4_href = crawling.blog4()
    blog5, blog5_href = crawling.blog5()
    blog6, blog6_href = crawling.blog6()
    blog7, blog7_href = crawling.blog7()
    blog8, blog8_href = crawling.blog8()
    blog9, blog9_href = crawling.blog9()
    blog10, blog10_href = crawling.blog10()
    blog11, blog11_href = crawling.blog11()


    return render_template("mobile.html",
                           list=myList, list_href=myList_href, list_len=len(myList),
                           list2=today, list2_href=today_href, list2_len=len(today),
                           list3=clien, list3_href=clien_href, list3_len=len(clien),
                           list4=blog, list4_href=blog_href, list4_len=len(blog),
                           list5=blog1, list5_href=blog1_href, list5_len=len(blog1),
                           list6=blog2, list6_href=blog2_href, list6_len=len(blog2),
                           list7=blog3, list7_href=blog3_href,  list7_len=len(blog3),
                           list8 = blog4, list8_href = blog4_href, list8_len = len(blog4),
                           list9 = blog5, list9_href = blog5_href, list9_len = len(blog5),
                           list10 = blog6, list10_href = blog6_href, list10_len = len(blog6),
                           list11 = blog7, list11_href = blog7_href, list11_len = len(blog7),
                           list12 = blog8, list12_href = blog8_href, list12_len = len(blog8),
                           list13 = blog9, list13_href = blog9_href, list13_len = len(blog9),
                           list14 = blog10, list14_href = blog10_href, list14_len = len(blog10),
                           list15 = blog11, list15_href = blog11_href, list15_len = len(blog11))


@app.route('/video')
def video():
    myList, myList_href = crawling.daum()
    today, today_href = crawling.today()
    clien, clien_href = crawling.clien()
    blog, blog_href = crawling.blog()
    blog1, blog1_href = crawling.blog1()
    blog2, blog2_href = crawling.blog2()
    blog3, blog3_href = crawling.blog3()
    blog4, blog4_href = crawling.blog4()
    blog5, blog5_href = crawling.blog5()



    return render_template("video.html",
                           list=myList, list_href=myList_href, list_len=len(myList),
                           list2=today, list2_href=today_href, list2_len=len(today),
                           list3=clien, list3_href=clien_href, list3_len=len(clien),
                           list4=blog, list4_href=blog_href, list4_len=len(blog),
                           list5=blog1, list5_href=blog1_href, list5_len=len(blog1),
                           list6=blog2, list6_href=blog2_href, list6_len=len(blog2),
                           list7=blog3, list7_href=blog3_href, list7_len=len(blog3),
                           list8=blog4, list8_href=blog4_href, list8_len=len(blog4),
                           list9=blog5, list9_href=blog5_href, list9_len=len(blog5)

                           )
#index1







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)