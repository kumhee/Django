from django.db import models
from django.contrib.auth.models import User

# 게시물 = POST
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey는 User 모델과 연결, 사용자정보 저장
    # on_delete=models.CASCADE는 게시물 작성자(User)가 삭제될 때 해당 게시물도 삭제되도록 설정
    
    # 게시물 작성 일자 및 시간을 자동으로 저장하는 필드
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # 게시물의 제목을 문자열로 반환


# 댓글
class Comment(models.Model):
    post = models.ForeignKey('board.Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
