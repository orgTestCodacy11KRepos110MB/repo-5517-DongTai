#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2020/10/23 12:00
# software: PyCharm
# project: webapi
import logging, requests, json
from django.utils.translation import gettext_lazy as _
from dongtai.models.agent_webhook_setting import IastAgentUploadTypeUrl

logger = logging.getLogger('dongtai.openapi')


class ReportHandler:
    HANDLERS = {}

    # 注册handler到当前命名空间，后续进行异步处理数据
    @staticmethod
    def handler(reports, user):
        """
        处理上传的报告，如果报告的类型不存在，则忽略本次上传；
        检查用户与agent的权限
        :param reports:
        :return:
        """
        try:
            report_type = reports.get('type')
            # 根据消息类型，转发上报到指定地址
            print(report_type)
            print(reports)
            typeData = IastAgentUploadTypeUrl.objects.filter(user=user, type_id=report_type).order_by("-create_time").first()
            if typeData and typeData.url:
                if typeData.headers:
                    headers = typeData.headers
                else:
                    headers = {}
                req = requests.post(typeData.url, json=reports, headers=headers)
                #
                if req.status_code == 200:
                    data = json.loads(req.text)
                    print(data)
                    if data.get("code", 0) == 200:
                        typeData.send_num = typeData.send_num+1
                        typeData.save()
            class_of_handler = ReportHandler.HANDLERS.get(report_type)
            if class_of_handler is None:
                logger.error(_('Report type {} handler does not exist').format(report_type))
                return None
            return class_of_handler().handle(reports, user)
        except Exception as e:
            logger.error(e)
        return None

    @classmethod
    def register(cls, handler_name):
        def wrapper(handler):
            logger.info(
                _('Registration report type {} handler {}').format(handler_name, handler.__name__))
            if handler_name not in cls.HANDLERS:
                cls.HANDLERS[handler_name] = handler
            return handler

        return wrapper
