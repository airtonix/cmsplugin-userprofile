## DjangoCMS UserProfile Plugin

This simple extension allows your admin users to embed a singular or
a group of user profile objects.

The freedom to change item and group container templates is there, meaning
that separate templates are used for the group, then another template for
each item in the group.

This allows for a great deal of theming flexibility post-deployment.

## Requirements

* django-cms
* django-profiles
* And all the requirements the above project(s) depend on.


## Installation

1. make sure you are using a python virtual environment

		virtualenv ~/Dev/virtualenv/projectname;
		. ~/Dev/virtualenv/projectname/bin/activate;
		cd ~/Dev/projects/projectname/;

2. install it from pypi

	`pip install cmsplugin-userprofiles`

3. or, install it from github

	`pip install git+https://github.com/airtonix/cmsplugin-userprofiles`


## Configuration

1. add `cmsplugin_userprofile` to `INSTALLED_APPS`

2. perform a `./manage.py migrate` (for south users), or `./manage.py syncdb`

3. There is no step three!


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

For example, if your django project was at :

	~/Dev/Django/MyProjectName/

And you had a django application named `SomethingSomethingSomething` at :

	~/Dev/Django/MyProjectName/SomethingSomethingSomething/

Then templates for this plugin could be found at :

	~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_userprofile

In fact, anywhere django looks for templates, you can place the following tree :

		cmsplugin_userprofile
			/containers
				/default.html
				/...

			/items
				/default.html
				/...

			/base.html

### Customising Templates

Templates in all groups are provided the context :

a CMSPlugin has many useful attributes for you to use, the main one
is `plugin.instance` a reference to the settings model.

>	 plugin' :
>		 An instance of CMSPlugin, which itself provides reference to either
>		 of the settings models as outlined below.

#### base.html

base.html in the `cmsplugin_configurableproduct` directory is used to load the
selected template chosen in the administration interface.


#### ./layouts/*.html

templates here are provided the context :

>	 plugin.instance
>		  template
>			   Chosen template.
>
>	 Pages
>		A list of cms.Page(s)




## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-userprofiles


## Todo

provide option to manipulate menu choices:

* Refine the product filter.
* Provide better default templates.
* Allow selecting/use of snippets for menu templates?
