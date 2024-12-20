New repository
随后来到本地项目，鼠标右击选择Git Bash Here
输入 git init
使用 git add . 添加文件
放入暂存区 git commit -m "first commit"    
注意如果出现 git config --global user.email "you@example.com" 和 git config --global user.name "Your Name"， 则you@example.com为GitHub邮箱，Your Name为GitHub名字
git branch -M main
git remote add scripts-dataset https://github.com/A0268/scripts-dataset.git
最后进行上传 git push -u scripts-dataset main
上传成功，刷新即可
