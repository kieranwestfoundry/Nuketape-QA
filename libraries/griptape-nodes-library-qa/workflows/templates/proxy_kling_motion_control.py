# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "proxy_Kling_Motion_Control"
# schema_version = "0.21.0"
# engine_version_created_with = "0.108.0"
# node_libraries_referenced = [["Griptape Nodes Library", "0.90.1"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "KlingMotionControl"], ["Griptape Nodes Library", "StartFlow"]]
# is_griptape_provided = false
# is_template = true
# is_internal = false
# creation_date = 2026-11-10T11:49:56.905571Z
# last_modified_date = 2026-11-10T11:52:04.311672Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"reference_image\":{\"name\":\"reference_image\",\"tooltip\":\"New parameter\",\"type\":\"ImageUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"ImageUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":true,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"reference_video\":{\"name\":\"reference_video\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":true,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"character_orientation\":{\"name\":\"character_orientation\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"video\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"character orientation\",\"hide_label\":false,\"hide_property\":false,\"simple_dropdown\":[\"image\",\"video\"],\"show_search\":true,\"search_filter\":\"\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"mode\":{\"name\":\"mode\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"pro\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"simple_dropdown\":[\"std\",\"pro\"],\"show_search\":true,\"search_filter\":\"\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"prompt\":{\"name\":\"prompt\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Optional: Add additional control with a text prompt...\",\"display_name\":\"prompt\",\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"video_url\":{\"name\":\"video_url\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"pulse_on_run\":true,\"clickable_file_browser\":true,\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}}}"
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
    top_level_unique_values_dict = {'fcbcf165908dd18a9e49f7ff27810176': False, '284b7e6d788f363f910f7beb1910473e': 600, '12ae32cb1ec02d01eda3581b127c1fee': '', '807f0525549ec1760febbccb23415a1d': 'video', '53cd6b72987929cb8e78fcad49cbacf6': 'pro', '4096fb69baf5880af1db016ae915003a': 'kling_motion_control.mp4'}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='KlingMotionControl', specific_library_name='Griptape Nodes Library', node_name='Kling Motion Control', metadata={'position': {'x': 1191.6666666666667, 'y': 496.66666666666674}, 'tempId': 'placing-1794311407110-uxn2dk', 'library_node_metadata': {'category': 'video', 'description': 'Transfer character actions from a reference video to a reference image using Kling Motion Control via Griptape Cloud model proxy.', 'display_name': 'Kling Motion Control', 'tags': ['video', 'motion-control', 'ai', 'api', 'kling'], 'icon': 'Sparkles', 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [{'type': 'model_usage', 'model_ids': ['gtc_kling_motion_control']}], 'resolved_model_usage': [{'providerId': 'kling', 'providerName': 'Kling AI', 'modelId': 'gtc_kling_motion_control', 'modelName': 'Kling Motion Control', 'family': 'Kling', 'keySupport': 'SUPPORTS_CUSTOMER_KEY_OR_GRIPTAPE_KEY'}]}, 'library': 'Griptape Nodes Library', 'node_type': 'KlingMotionControl', 'showaddparameter': False, 'size': {'width': 600, 'height': 948}}, initial_setup=True))).node_name
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'position': {'x': 330.91475032787366, 'y': 749.1666666666667}, 'tempId': 'placing-1794311453490-whxbji', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 443}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='reference_image', default_value='', tooltip='New parameter', type='ImageUrlArtifact', input_types=['any'], output_type='ImageUrlArtifact', ui_options={'clickable_file_browser': True, 'hide_label': False, 'hide_property': True, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='reference_video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['any'], output_type='VideoUrlArtifact', ui_options={'clickable_file_browser': True, 'hide_label': False, 'hide_property': True, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='character_orientation', default_value='video', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'display_name': 'character orientation', 'hide_label': False, 'hide_property': False, 'simple_dropdown': ['image', 'video'], 'show_search': True, 'search_filter': '', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='mode', default_value='pro', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'hide_label': False, 'hide_property': False, 'simple_dropdown': ['std', 'pro'], 'show_search': True, 'search_filter': '', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='prompt', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'multiline': True, 'placeholder_text': 'Optional: Add additional control with a text prompt...', 'display_name': 'prompt', 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'position': {'x': 1989.317996458248, 'y': 540.2354536561213}, 'tempId': 'placing-1794311497657-ea2u7', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 300}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video_url', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['any'], output_type='VideoUrlArtifact', ui_options={'pulse_on_run': True, 'clickable_file_browser': True, 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='reference_image', target_node_name=node0_name, target_parameter_name='reference_image', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='reference_video', target_node_name=node0_name, target_parameter_name='reference_video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='character_orientation', target_node_name=node0_name, target_parameter_name='character_orientation', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='mode', target_node_name=node0_name, target_parameter_name='mode', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='video_url', target_node_name=node2_name, target_parameter_name='video_url', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='failure', target_node_name=node2_name, target_parameter_name='failed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='prompt', target_node_name=node0_name, target_parameter_name='prompt', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='exec_out', target_node_name=node0_name, target_parameter_name='exec_in', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='api_key_provider', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='timeout', node_name=node0_name, value=decode_value(top_level_unique_values_dict['284b7e6d788f363f910f7beb1910473e']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='keep_original_sound', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='character_orientation', node_name=node0_name, value=decode_value(top_level_unique_values_dict['807f0525549ec1760febbccb23415a1d']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='mode', node_name=node0_name, value=decode_value(top_level_unique_values_dict['53cd6b72987929cb8e78fcad49cbacf6']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node0_name, value=decode_value(top_level_unique_values_dict['4096fb69baf5880af1db016ae915003a']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='reference_image', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='reference_video', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='character_orientation', node_name=node1_name, value=decode_value(top_level_unique_values_dict['807f0525549ec1760febbccb23415a1d']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='mode', node_name=node1_name, value=decode_value(top_level_unique_values_dict['53cd6b72987929cb8e78fcad49cbacf6']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
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
    parser.add_argument('--reference_image', dest='reference_image', default=None, help='New parameter')
    parser.add_argument('--reference_video', dest='reference_video', default=None, help='New parameter')
    parser.add_argument('--character_orientation', dest='character_orientation', default=None, help='New parameter')
    parser.add_argument('--mode', dest='mode', default=None, help='New parameter')
    parser.add_argument('--prompt', dest='prompt', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.reference_image is not None:
            flow_input['Start Flow']['reference_image'] = args.reference_image
        if args.reference_video is not None:
            flow_input['Start Flow']['reference_video'] = args.reference_video
        if args.character_orientation is not None:
            flow_input['Start Flow']['character_orientation'] = args.character_orientation
        if args.mode is not None:
            flow_input['Start Flow']['mode'] = args.mode
        if args.prompt is not None:
            flow_input['Start Flow']['prompt'] = args.prompt
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
