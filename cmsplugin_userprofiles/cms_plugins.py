from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from models import (
	UserSettings,
	GroupSettings,
	ApplicationSettings,
)

class UserProfilePlugin(CMSPluginBase):
	model = UserSettings
	name = _("UserProfile: Single Profile")
	render_template = "cmsplugin_userprofile/user/base.html"
	admin_preview = False

	def render(self, context, instance, placeholder):
		return context

plugin_pool.register_plugin(UserProfilePlugin)


class UserProfileListPlugin(CMSPluginBase):
	model = GroupSettings
	name = _("UserProfile: Group List")
	render_template = "cmsplugin_userprofile/list/base.html"
	admin_preview = False

	def render(self, context, instance, placeholder):
		chosen_groups = instance.groups
		users = users = User.objects.filter(
				groups__in=chosen_groups.all().values('id')
			)

		if instance.sort:

			sort_direction = instance.sort_direction
			if not sort_direction:
				sort_direction = ""

			users = users.order_by("{0}{1}".format(
				sort_direction,
				instance.sort
			))

		users = users.filter(userprofile__public=True)

		context.update({
			"Users": users,
			"Groups": chosen_groups
		})
		return context

plugin_pool.register_plugin(UserProfileListPlugin)
