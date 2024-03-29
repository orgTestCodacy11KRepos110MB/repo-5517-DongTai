#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/9/28 上午10:51
# project: dongtai-openapi
from drf_spectacular.utils import OpenApiParameter, OpenApiExample


class DongTaiAuth:
    TOKEN = 'TokenAuthentication'


class DongTaiParameter:
    OPENAPI_URL = OpenApiParameter(
        name='url',
        description='OpenAPI Service Addr',
        required=True,
        type=str,
        examples=[
            OpenApiExample(
                'url example',
                summary='default',
                value='https://openapi.iast.io',
            ),
        ],
    )
    PROJECT_NAME = OpenApiParameter(
        name='projectName',
        type=str,
        description='The name of the project where the Agent needs to be installed',
        examples=[
            OpenApiExample(
                'example with https://iast.io',
                summary='default',
                value='Demo Project',
            ),
        ],
    )

    LANGUAGE = OpenApiParameter(
        name='language',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='JAVA or PYTHON',
                value='JAVA',
            ),
        ],
    )

    VERSION = OpenApiParameter(
        name='version',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    AGENT_NAME = OpenApiParameter(
        name='name',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    HOSTNAME = OpenApiParameter(
        name='engineName',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    NETWORK = OpenApiParameter(
        name='engineName',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    CONTAINER_NAME = OpenApiParameter(
        name='containerName',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    SERVER_ADDR = OpenApiParameter(
        name='serverAddr',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    SERVER_PORT = OpenApiParameter(
        name='serverPort',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    SERVER_PATH = OpenApiParameter(
        name='serverPath',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    SERVER_ENV = OpenApiParameter(
        name='serverEnv',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    PID = OpenApiParameter(
        name='pid',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )

    AUTO_CREATE_PROJECT = OpenApiParameter(
        name='autoCreateProject',
        type=int,
        description='auto create project if project not found when this varibale is 1',
        required=True,
        examples=[
            OpenApiExample(
                'default value',
                value=0,
            ),
            OpenApiExample(
                'enable value',
                value=1,
            ),
        ],
    )
    ENGINE_NAME = OpenApiParameter(
        name='engineName',
        type=str,
        description='The development language of the project that needs to install the Agent',
        required=True,
        examples=[
            OpenApiExample(
                'example language',
                summary='java or python',
                value='java',
            ),
        ],
    )
