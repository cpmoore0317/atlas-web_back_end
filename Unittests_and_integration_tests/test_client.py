#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "test"})
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns the correct URL."""
        expected_url = "https://api.github.com/orgs/test_org/repos"
        mock_org.return_value = {"repos_url": expected_url}

        client = GithubOrgClient("test_org")
        result = client._public_repos_url

        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct list of repos."""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        expected_repos = ["repo1", "repo2", "repo3"]

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")
            self.assertEqual(result, expected_repos)


if __name__ == '__main__':
    unittest.main()
