# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class WorkItemFieldOperation(Model):
    """WorkItemFieldOperation.

    :param name:
    :type name: str
    :param reference_name:
    :type reference_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'}
    }

    def __init__(self, name=None, reference_name=None):
        super(WorkItemFieldOperation, self).__init__()
        self.name = name
        self.reference_name = reference_name
