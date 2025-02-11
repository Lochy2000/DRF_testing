# from django.contrib.auth.models import User
# from .models import Post
# from rest_framework import status
# from rest_framework.test import APITestCase


# # Create your tests here.

# class PostListViewTests(APITestCase):

#     def setUp(self):
#         User.objects.create_user(username='adam', password='pass')

#     def test_can_list_posts(self):
#         adam = User.objects.get(username='adam')
#         Post.objects.create(owner=adam, title='a title')
#         response = self.client.get('/posts/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(response.data)
#         print(len(response.data))

#     def test_logged_in_user_can_create_post(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.post('/posts/', {'title': 'a title'})
#         count = Post.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_logged_out_user_cannot_create_post(self):
#         response = self.client.post('/posts/', {'title': 'a title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         count = Post.objects.count()
#         self.assertEqual(count, 0)

# class PostDetailViewTests(APITestCase):
#     def setUp(self):
#         # Create two users
#         self.user = User.objects.create_user(username='adam', password='pass')
#         self.user2 = User.objects.create_user(username='brian', password='pass')
#         # Create a post for our tests
#         Post.objects.create(
#             owner=self.user,
#             title='adams post',
#             content='adams content'
#         )
#         Post.objects.create(
#             owner=self.user2,
#             title='brians post',
#             content='brians content'
#         ) 
    
#     def test_can_retrieve_post_using_valid_id(self):
#         response = self.client.get('/posts/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'adams post')

#     def test_cant_retrieve_post_using_invalid_id(self):
#         response = self.client.get('/posts/999/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_own_post(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.put('/posts/1/', {'title': 'updated title'})
#         post = Post.objects.filter(pk=1).first()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'updated title')

#     def test_user_cant_update_another_users_post(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.put('/posts/2/', {'title': 'updated title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)