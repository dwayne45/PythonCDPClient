from cdp_client import cdp_pb2 as proto
from copy import copy

value1 = proto.VariantValue()
value1.node_id = 5
value1.d_value = 55
value1.timestamp = 777

value2 = proto.VariantValue()
value2.node_id = 5
value2.d_value = 66
value2.timestamp = 888

value1_node = proto.Node()
value1_node.info.node_id = 5
value1_node.info.name = "Value1"
value1_node.info.node_type = proto.CDP_PROPERTY
value1_node.info.value_type = proto.eDOUBLE
value1_node.info.flags = proto.Info.eNodeIsLeaf

app1_node = proto.Node()
app1_node.info.node_id = 1
app1_node.info.name = "App1"
app1_node.info.node_type = proto.CDP_APPLICATION
app1_node.info.value_type = proto.eUNDEFINED
app1_node.info.flags = proto.Info.eValueIsReadOnly | proto.Info.eNodeIsLeaf

app2_node = proto.Node()
app2_node.info.node_id = 2
app2_node.info.name = "App2"
app2_node.info.node_type = proto.CDP_APPLICATION
app2_node.info.value_type = proto.eUNDEFINED
app2_node.info.flags = proto.Info.eValueIsReadOnly

app3_node = proto.Node()
app3_node.info.node_id = 3
app3_node.info.name = "App3"
app3_node.info.node_type = proto.CDP_APPLICATION
app3_node.info.value_type = proto.eUNDEFINED
app3_node.info.flags = proto.Info.eValueIsReadOnly

system_node = proto.Node()
system_node.info.node_id = 0
system_node.info.name = "System"
system_node.info.node_type = proto.CDP_SYSTEM
system_node.info.value_type = proto.eUNDEFINED
system_node.info.flags = proto.Info.eValueIsReadOnly

hello_response = proto.Hello()
hello_response.system_name = "foo"
hello_response.compat_version = 1
hello_response.incremental_version = 0


def create_system_structure_response():
    response = proto.Container()
    response.message_type = proto.Container.eStructureResponse
    system = copy(system_node)
    system.node.extend([copy(app1_node), copy(app2_node)])
    response.structure_response.extend([system])
    return response


def create_app_structure_response():
    response = proto.Container()
    response.message_type = proto.Container.eStructureResponse
    app = copy(app2_node)
    app.node.extend([copy(value1_node)])
    response.structure_response.extend([app])
    return response


def create_app_structure_change_response():
    response = proto.Container()
    response.message_type = proto.Container.eStructureChangeResponse
    response.structure_change_response.extend([app1_node.info.node_id])
    return response


def create_value_response():
    response = proto.Container()
    response.message_type = proto.Container.eGetterResponse
    response.getter_response.extend([value1])
    return response


def create_error_response():
    response = proto.Container()
    response.message_type = proto.Container.eRemoteError
    response.error.code = proto.eINVALID_REQUEST
    response.error.text = "foo"
    return response