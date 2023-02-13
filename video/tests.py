import unittest
from django.test import TestCase
from .models import Video, Comment, Like, User
from django.contrib.auth.models import User

user = Video.objects.all()[0].user


class VideoModelTestCase(TestCase): # testing Django model video object
    def setUp(self):
        self.video = Video(name="testvideo",
                            user=user,
                            description="A test video",
                            category="Sport")


    def test_video_model_creation(self):
        self.assertTrue(isinstance(self.video, Video))
        self.assertEqual(self.video.name, 'testvideo')
        self.assertEqual(self.video.description, 'A test video')
        self.assertEqual(self.video.category, 'Sport')


class CommentModelTestCase(TestCase): # testing django comment model object
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.video = Video.objects.create(user=self.user,
                                         name="testvideo",
                                         description="A test video",
                                         category="Sport")

        self.comment = Comment.objects.create(
            video=self.video,
            author=self.user,
            content="This is a test comment",)

    def test_comment_model_creation(self): 
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(self.comment.content, 'This is a test comment')
        self.assertEqual(self.comment.video, self.video)
        self.assertEqual(self.comment.author, self.user)


class LikeModelTestCase(TestCase): # testing django like model object
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.video = Video.objects.create(user=self.user,
                                         name="testvideo",
                                         description="A test video",
                                         category="Sport")
        self.like = Like.objects.create(
            video=self.video,
            user=self.user
        )

    def test_like_model_creation(self):
        self.assertTrue(isinstance(self.like, Like))
        self.assertEqual(self.like.video, self.video)
        self.assertEqual(self.like.user, self.user)