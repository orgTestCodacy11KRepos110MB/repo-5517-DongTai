#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:sjh
# software: PyCharm
# project: lingzhi-webapi
import logging
import time
from dongtai_common.endpoint import UserEndPoint, R
from dongtai_common.models.project_version import IastProjectVersion
from dongtai_common.models.project import IastProject
from dongtai_common.models.agent import IastAgent
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger("django")


class UpdateProjectVersion(UserEndPoint):
    name = "api-v1-project-version-check"
    description = _("Detects and associates application version information")

    def get(self, request):
        try:
            all_project = IastProject.objects.all()
            data = []
            for one in all_project:
                result = IastProjectVersion.objects.filter(project_id=one.id, user_id=one.user_id, status=1).first()
                if not result:
                    result = IastProjectVersion.objects.create(
                        version_name="V1.0",
                        project_id=one.id,
                        user_id=one.user_id,
                        current_version=1,
                        status=1
                    )
                    data.append(result.id)
                IastAgent.objects.filter(
                    bind_project_id=one.id,
                    user_id=one.user_id,
                    project_version_id=0
                ).update(
                    project_version_id=result.id,
                    latest_time=int(time.time())
                )
            return R.success(msg=_('Detection finished'), data=data)
        except Exception as e:
            return R.failure(status=202, msg=_('Detection failed'))
