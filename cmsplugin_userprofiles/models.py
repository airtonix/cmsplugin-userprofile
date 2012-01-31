import os
from os.path import join, getsize

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

from cms.models.pluginmodel import CMSPlugin

from appconf import AppConf

from .lib.choices import (
	DynamicTemplateChoices,
	)

class ApplicationSettings(AppConf):
		FEATUREDITEMS_LIST_TEMPLATES = "cmsplugin_userprofile/list/container"
		FEATUREDITEMS_ITEM_TEMPLATES = "cmsplugin_userprofile/list/item"

class UserSettings(CMSPlugin):
		group_title = models.CharField(max_length = 128, default="Users")


class GroupSettings(CMSPlugin):
		group_title = models.CharField(max_length = 128, default="Users", blank=True, null=True)

		groups = models.ManyToManyField(Group,
			help_text=_('Groups to look for users in'))

		sort = models.CharField(default="date_joined", blank=True, null=True,
			max_length=128,
			choices = (
				("date_joined", 'User: Created'),
				("last_login", 'User: Last Login'),
				("id", 'User: Id'),
				("last_name", 'User: Last Name'),
				("first_name", 'User: First Name'),
				("username", 'User: Username'),
				("userprofile__screenname", 'UserProfile: Screenname'),
				("userprofile__title", 'UserProfile: Title'),
			),
			help_text=_('How to sort the results?'))

		sort_direction = models.CharField(default="", blank=True, null=True,
			max_length=128,
			choices = (
				("", 'Descending'),
				("-", 'Asscending'),
			),
			help_text=_('How to sort the results?'))

		match = models.CharField(default="or",
			max_length=32, blank=True, null=True,
			choices = (
				("and", "User is in all groups"),
				("or", "User is in any of the groups")
			),
			help_text=_("""OR: present in any of the selected groups,
										 AND: present in all groups."""))

		container_template = models.CharField(choices=DynamicTemplateChoices(
																	path=ApplicationSettings.FEATUREDITEMS_LIST_TEMPLATES,
																	include='.html'),
				max_length=256, blank=True, null=True,
				default = ('default', os.path.join(ApplicationSettings.FEATUREDITEMS_LIST_TEMPLATES, "default.html")),
				help_text="""Select a template to render this
						list. Templates are stored in : {0}""".format(
							ApplicationSettings.FEATUREDITEMS_LIST_TEMPLATES))

		item_template = models.CharField(choices=DynamicTemplateChoices(
																	path=ApplicationSettings.FEATUREDITEMS_ITEM_TEMPLATES,
																	include='.html'),
				max_length=256, blank=True, null=True,
				default = os.path.join(ApplicationSettings.FEATUREDITEMS_ITEM_TEMPLATES,
			"default.html"),
					help_text="""Select a template to render the items in the list.
						Templates are stored in : {0}""".format(
							ApplicationSettings.FEATUREDITEMS_ITEM_TEMPLATES))
