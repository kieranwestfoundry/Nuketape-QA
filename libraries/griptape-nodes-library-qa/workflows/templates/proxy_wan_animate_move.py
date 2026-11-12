# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "proxy_WAN_ANIMATE_MOVE"
# schema_version = "0.21.0"
# engine_version_created_with = "0.108.0"
# node_libraries_referenced = [["Griptape Nodes Library", "0.90.1"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "StartFlow"], ["Griptape Nodes Library", "WanAnimateGeneration"]]
# is_griptape_provided = false
# is_template = true
# is_internal = false
# creation_date = 2026-11-10T10:12:06.325100Z
# last_modified_date = 2026-11-10T10:14:19.047892Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"image_url\":{\"name\":\"image_url\",\"tooltip\":\"New parameter\",\"type\":\"ImageUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"ImageUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Image URL\",\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":true,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"video_url\":{\"name\":\"video_url\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Video URL\",\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":true,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"model\":{\"name\":\"model\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"wan2.2-animate-move\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"data\":[{\"name\":\"wan2.2-animate-mix\",\"label\":\"Wan 2.2 Animate Mix\"},{\"name\":\"wan2.2-animate-move\",\"label\":\"Wan 2.2 Animate Move\"}],\"dropdown_row_icons\":true,\"dropdown_row_subtitles\":true,\"simple_dropdown\":[\"wan2.2-animate-mix\",\"wan2.2-animate-move\",\"Wan 2.2 Animate Mix\",\"Wan 2.2 Animate Move\",\"gtc_wan_2_2_animate_mix\",\"gtc_wan_2_2_animate_move\"],\"show_search\":true,\"search_filter\":\"\",\"button_label\":\"\",\"variant\":\"secondary\",\"size\":\"icon\",\"state\":\"normal\",\"full_width\":false,\"button_icon\":\"list-restart\",\"iconPosition\":\"left\",\"tooltip\":\"Refresh available models\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"mode\":{\"name\":\"mode\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"wan-pro\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"simple_dropdown\":[\"wan-std\",\"wan-pro\"],\"show_search\":true,\"search_filter\":\"\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"video\":{\"name\":\"video\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"pulse_on_run\":true,\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}}}"
# 
# ///

import argparse
import asyncio
import json
import logging
from griptape_nodes.bootstrap.workflow_executors.local_workflow_executor import LocalWorkflowExecutor
from griptape_nodes.bootstrap.workflow_executors.workflow_executor import WorkflowExecutor
from griptape_nodes.node_library.library_registry import IconVariant, NodeDeprecationMetadata, NodeMetadata
from griptape_nodes.retained_mode.events.connection_events import CreateConnectionRequest
from griptape_nodes.retained_mode.events.flow_events import CreateFlowRequest, GetTopLevelFlowRequest, GetTopLevelFlowResultSuccess
from griptape_nodes.retained_mode.events.library_events import RegisterLibraryFromFileRequest
from griptape_nodes.retained_mode.events.node_events import CreateNodeRequest
from griptape_nodes.retained_mode.events.parameter_events import AddParameterToNodeRequest, AlterParameterDetailsRequest, SetParameterValueRequest
from griptape_nodes.retained_mode.griptape_nodes import GriptapeNodes
from griptape_nodes.serialization.values import decode_value
from typing import Any

async def build_workflow() -> None:
    await GriptapeNodes.ahandle_request(RegisterLibraryFromFileRequest(library_name='Griptape Nodes Library', perform_discovery_if_not_found=True))
    # Every unique parameter value, stored once and keyed by a hash of its content.
    # Values that aren't plain data carry a '$type' naming their class; decode_value rebuilds them.
    top_level_unique_values_dict = {'fcbcf165908dd18a9e49f7ff27810176': False, '284b7e6d788f363f910f7beb1910473e': 600, '4e48f2e1f576df09241bb8132629fefb': 'wan2.2-animate-move', '410b629bf136b0172f9217a62f984d10': 'wan-pro', '99b1e00e45cec222e5a5c4cc215db539': 'wan_animate.mp4', '12ae32cb1ec02d01eda3581b127c1fee': ''}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='WanAnimateGeneration', specific_library_name='Griptape Nodes Library', node_name='WAN Animate Generation', metadata={'position': {'x': 1000, 'y': 393.33333333333326}, 'tempId': 'placing-1794305557719-93o29o', 'library_node_metadata': {'category': 'video', 'description': 'Generate animated videos from images using WAN Animate models via Griptape model proxy', 'display_name': 'WAN Animate Generation', 'tags': ['video', 'animation', 'ai', 'api', 'wan'], 'icon': 'Sparkles', 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [{'type': 'model_usage', 'model_ids': ['gtc_wan_2_2_animate_mix', 'gtc_wan_2_2_animate_move']}], 'resolved_model_usage': [{'providerId': 'dashscope', 'providerName': 'Alibaba Cloud Model Studio', 'modelId': 'gtc_wan_2_2_animate_mix', 'modelName': 'Wan 2.2 Animate Mix', 'family': 'Wan', 'keySupport': 'SUPPORTS_CUSTOMER_KEY_OR_GRIPTAPE_KEY'}, {'providerId': 'dashscope', 'providerName': 'Alibaba Cloud Model Studio', 'modelId': 'gtc_wan_2_2_animate_move', 'modelName': 'Wan 2.2 Animate Move', 'family': 'Wan', 'keySupport': 'SUPPORTS_CUSTOMER_KEY_OR_GRIPTAPE_KEY'}]}, 'library': 'Griptape Nodes Library', 'node_type': 'WanAnimateGeneration', 'size': {'width': 400, 'height': 760}, 'showaddparameter': False}, initial_setup=True))).node_name
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'position': {'x': -25.138441887817063, 'y': 517.9754122931637}, 'tempId': 'placing-1794305590865-bjbzmn', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 315}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='image_url', default_value='', tooltip='New parameter', type='ImageUrlArtifact', input_types=['any'], output_type='ImageUrlArtifact', ui_options={'display_name': 'Image URL', 'clickable_file_browser': True, 'hide_label': False, 'hide_property': True, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video_url', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['any'], output_type='VideoUrlArtifact', ui_options={'display_name': 'Video URL', 'clickable_file_browser': True, 'hide_label': False, 'hide_property': True, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='model', default_value='wan2.2-animate-move', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'hide_label': False, 'hide_property': False, 'data': [{'name': 'wan2.2-animate-mix', 'label': 'Wan 2.2 Animate Mix'}, {'name': 'wan2.2-animate-move', 'label': 'Wan 2.2 Animate Move'}], 'dropdown_row_icons': True, 'dropdown_row_subtitles': True, 'simple_dropdown': ['wan2.2-animate-mix', 'wan2.2-animate-move', 'Wan 2.2 Animate Mix', 'Wan 2.2 Animate Move', 'gtc_wan_2_2_animate_mix', 'gtc_wan_2_2_animate_move'], 'show_search': True, 'search_filter': '', 'button_label': '', 'variant': 'secondary', 'size': 'icon', 'state': 'normal', 'full_width': False, 'button_icon': 'list-restart', 'iconPosition': 'left', 'tooltip': 'Refresh available models', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='mode', default_value='wan-pro', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'hide_label': False, 'hide_property': False, 'simple_dropdown': ['wan-std', 'wan-pro'], 'show_search': True, 'search_filter': '', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'position': {'x': 1846.6666666666667, 'y': 435.0000000000001}, 'tempId': 'placing-1794305617764-1rpkia', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 300}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['any'], output_type='VideoUrlArtifact', ui_options={'pulse_on_run': True, 'clickable_file_browser': True, 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='image_url', target_node_name=node0_name, target_parameter_name='image_url', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='video_url', target_node_name=node0_name, target_parameter_name='video_url', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='model', target_node_name=node0_name, target_parameter_name='model', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='mode', target_node_name=node0_name, target_parameter_name='mode', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='video', target_node_name=node2_name, target_parameter_name='video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='failure', target_node_name=node2_name, target_parameter_name='failed', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='api_key_provider', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='timeout', node_name=node0_name, value=decode_value(top_level_unique_values_dict['284b7e6d788f363f910f7beb1910473e']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node0_name, value=decode_value(top_level_unique_values_dict['4e48f2e1f576df09241bb8132629fefb']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='mode', node_name=node0_name, value=decode_value(top_level_unique_values_dict['410b629bf136b0172f9217a62f984d10']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node0_name, value=decode_value(top_level_unique_values_dict['99b1e00e45cec222e5a5c4cc215db539']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='image_url', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='video_url', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node1_name, value=decode_value(top_level_unique_values_dict['4e48f2e1f576df09241bb8132629fefb']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='mode', node_name=node1_name, value=decode_value(top_level_unique_values_dict['410b629bf136b0172f9217a62f984d10']), initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node2_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))

async def _ensure_workflow_context():
    context_manager = GriptapeNodes.ContextManager()
    if not context_manager.has_current_flow():
        top_level_flow_request = GetTopLevelFlowRequest()
        top_level_flow_result = await GriptapeNodes.ahandle_request(top_level_flow_request)
        if isinstance(top_level_flow_result, GetTopLevelFlowResultSuccess) and top_level_flow_result.flow_name is not None:
            flow_manager = GriptapeNodes.FlowManager()
            flow_obj = flow_manager.get_flow_by_name(top_level_flow_result.flow_name)
            context_manager.push_flow(flow_obj)

def execute_workflow(input: dict, *, workflow_executor: WorkflowExecutor | None=None, **kwargs: Any) -> dict | None:
    return asyncio.run(aexecute_workflow(input=input, workflow_executor=workflow_executor, **kwargs))

async def aexecute_workflow(input: dict, *, workflow_executor: WorkflowExecutor | None=None, **kwargs: Any) -> dict | None:
    if workflow_executor is None:
        workflow_executor = LocalWorkflowExecutor(skip_library_loading=True, workflows_to_register=[__file__], **kwargs)
    async with workflow_executor as executor:
        GriptapeNodes.ContextManager().push_workflow(file_path=__file__)
        await build_workflow()
        await _ensure_workflow_context()
        await executor.arun(flow_input=input, **kwargs)
    return executor.output

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    LocalWorkflowExecutor.add_cli_arguments(parser)
    parser.add_argument('--json-input', default=None, help='JSON string containing parameter values. Takes precedence over individual parameter arguments if provided.')
    parser.add_argument('--exec_out', dest='exec_out', default=None, help='Connection to the next node in the execution chain')
    parser.add_argument('--image_url', dest='image_url', default=None, help='New parameter')
    parser.add_argument('--video_url', dest='video_url', default=None, help='New parameter')
    parser.add_argument('--model', dest='model', default=None, help='New parameter')
    parser.add_argument('--mode', dest='mode', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.image_url is not None:
            flow_input['Start Flow']['image_url'] = args.image_url
        if args.video_url is not None:
            flow_input['Start Flow']['video_url'] = args.video_url
        if args.model is not None:
            flow_input['Start Flow']['model'] = args.model
        if args.mode is not None:
            flow_input['Start Flow']['mode'] = args.mode
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
