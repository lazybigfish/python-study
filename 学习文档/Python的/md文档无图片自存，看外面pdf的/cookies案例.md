# post请求

其实，post和get都可以带着参数请求，不过get请求的参数会在url上显示出来。

但post请求的参数就不会直接显示，而是隐藏起来。像账号密码这种私密的信息，就应该用post的请求。如果用get请求的话，账号密码全部会显示在网址上，这显然不科学！你可以这么理解，get是明文显示，post是非明文显示。

通常，get请求会应用于获取网页数据，比如我们之前学的requests.get()。post请求则应用于向网页提交数据，比如提交表单类型数据（像账号密码就是网页表单的数据）。

get和post是两种最常用的请求方式，除此之外，还有其他类型的请求方式，如head、options等，这里我们就不详讲了，因为一般很少用到。

---

正如【requests headers】存储的是浏览器的请求信息，【response headers】存储的是服务器的响应信息。我们这一关要找的cookies就在其中。

---

## cookies及其用法

其实，你对cookies并不陌生，我敢肯定你见过它。比如一般当你登录一个网站，你都会在登录页面看到一个可勾选的选项“记住我”，如果你勾选了，以后你再打开这个网站就会自动登录，这就是cookie在起作用。

数据存放在 from data。

