from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    # Setup function is a function that will be run before every test that we run
    # Good when you need something done before every test case
    # Create a superuser, log him in and create a normal user

    def setUp(self):
        """Create a superuser and log him in
                    Create a user"""
        # Creating a client - mock?
        self.client = Client()
        # Creating an admin(superuser) - mock?
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@vienna.com',
            password='testPassword123'
        )
        # force_login is a helper function from the client, it allows us to log in a user with Django authentication
        # Makes tests easier to write as we don't have to log in manually, login with our admin user
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@vienna.com',
            password='testUserPassword123',
            name='Test user full_name'
        )

    def test_users_listed(self):
        """Test that users are listed in user page.
        We have to make changes to django admin to accommodate
        our custom user model"""

        # These urls are listed in django admin docs
        # 'admin:core_user_changelist' -> Gets the URL that lists users in admin page
        # 'admin:core_user_change'
        # 'admin:core_user_add'

        # Gets the URL that lists users in admin page
        # have to register User model to admin for this url to work
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test the user edit page works"""

        # We have to include fieldsets to UserAdmin for this to work
        url = reverse('admin:core_user_change', args=[self.user.id])
        # :id -> args, this is how they work in the reverse function
        # /admin/core/user/:id -> /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
