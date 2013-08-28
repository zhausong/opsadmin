from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^$','dashboard.views.index'),
      url(r'^index/','dashboard.views.index'),
      url(r'^login/','dashboard.views.login'),
      url(r'^register/','opsadmin.views.register'),
      url(r'^logout/','dashboard.views.logout'),
      url(r'^idc-manager/','idcmanager.views.idc'),
      url(r'^add_tab/','idcmanager.views.add_tab'),
      url(r'^add_idc_name/','idcmanager.views.add_idc_name'),
      url(r'^add_location_name/','idcmanager.views.add_location_name'),
      url(r'^saltstack/','saltstack.views.saltstack'),
      url(r'^saltstack_master_config/','saltstack.views.saltstack_master_config'),
      url(r'^saltstack_master_group','saltstack.views.saltstack_master_group'),
      url(r'^saltstack_top_sls','saltstack.views.saltstack_top_sls'),
      url(r'^saltstack_os_path_edit','saltstack.views.os_path_edit'),
      url(r'^ssh_remote_manager','saltstack.views.ssh_remote_manager'),
      url(r'^salt_key/','saltstack.views.salt_key'),
)
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
