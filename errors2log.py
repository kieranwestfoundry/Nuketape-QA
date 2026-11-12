# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "Errors2Log"
# schema_version = "0.21.0"
# engine_version_created_with = "0.109.0"
# node_libraries_referenced = [["QA Test Nodes", "0.1.0"], ["Griptape Nodes Library", "0.90.3"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "StartFlow"], ["QA Test Nodes", "EmitLogSeverity"]]
# description = "Workflow with a node that purposefully errors. For testing Nuke-tape Log"
# is_griptape_provided = false
# is_template = false
# is_internal = false
# creation_date = 2026-11-12T13:59:59.285955Z
# last_modified_date = 2026-11-12T14:20:22.547106Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"message\":{\"name\":\"message\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"QA test message\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"multiline\":true,\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"severity\":{\"name\":\"severity\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"ERROR\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"simple_dropdown\":[\"WARNING\",\"ERROR\"],\"show_search\":true,\"search_filter\":\"\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"fail_node_on_error\":{\"name\":\"fail_node_on_error\",\"tooltip\":\"New parameter\",\"type\":\"bool\",\"input_types\":[\"any\"],\"output_type\":\"bool\",\"default_value\":true,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"severity\":{\"name\":\"severity\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"simple_dropdown\":[\"WARNING\",\"ERROR\"],\"show_search\":true,\"search_filter\":\"\",\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"message\":{\"name\":\"message\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"multiline\":true,\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"fail_node_on_error\":{\"name\":\"fail_node_on_error\",\"tooltip\":\"New parameter\",\"type\":\"bool\",\"input_types\":[\"any\"],\"output_type\":\"bool\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}}}"
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
    await GriptapeNodes.ahandle_request(RegisterLibraryFromFileRequest(library_name='QA Test Nodes', perform_discovery_if_not_found=True))
    await GriptapeNodes.ahandle_request(RegisterLibraryFromFileRequest(library_name='Griptape Nodes Library', perform_discovery_if_not_found=True))
    # Every unique parameter value, stored once and keyed by a hash of its content.
    # Values that aren't plain data carry a '$type' naming their class; decode_value rebuilds them.
    top_level_unique_values_dict = {'0328987e655ccda6e67c8fc15e75e624': 'QA test message', 'f717e7d817dbc0e03438173773012fc4': 'ERROR', 'b5bea41b6c623f7c09f1bf24dcae58eb': True, '6f51c458d9fa5d13a394f9d3e673cb6e': 'ERROR: [Emit Warning / Error] QA test message', '13d5bb126f2602fdfac6dceeb7c847be': 'Control Input Selection', 'eec80c33d01a30822ada8a44d78f23c2': '[SUCCEEDED]\n[SUCCEEDED]\nNo details supplied by flow'}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'position': {'x': 402.5914885922401, 'y': 443.33333333333326}, 'tempId': 'placing-1794492014382-onx7g9', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 332}}, resolution='resolved', initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='message', default_value='QA test message', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'multiline': True, 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='severity', default_value='WARNING', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'hide_label': False, 'hide_property': False, 'simple_dropdown': ['WARNING', 'ERROR'], 'show_search': True, 'search_filter': '', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='fail_node_on_error', default_value=True, tooltip='New parameter', type='bool', input_types=['any'], output_type='bool', ui_options={'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EmitLogSeverity', specific_library_name='QA Test Nodes', node_name='Emit Warning / Error', metadata={'position': {'x': 1112.816675717073, 'y': 403.33333333333326}, 'tempId': 'placing-1794492523350-4zhl45', 'library_node_metadata': {'category': 'qa', 'description': 'WARNING logs to the engine log. ERROR fails the node (NodeErrorEvent), which the Nuke bridge forwards.', 'display_name': 'Emit Warning / Error', 'tags': ['qa', 'debug', 'log', 'error', 'warning'], 'icon': 'triangle-alert', 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'QA Test Nodes', 'node_type': 'EmitLogSeverity', 'showaddparameter': False, 'size': {'width': 600, 'height': 412}}, initial_setup=True))).node_name
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'position': {'x': 1855.848945811112, 'y': 403.33333333333326}, 'tempId': 'placing-1794492584837-q8hetd', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'size': {'width': 626, 'height': 521}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='severity', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'hide_label': False, 'hide_property': False, 'simple_dropdown': ['WARNING', 'ERROR'], 'show_search': True, 'search_filter': '', 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='message', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'multiline': True, 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='fail_node_on_error', default_value='', tooltip='New parameter', type='bool', input_types=['any'], output_type='bool', ui_options={'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='message', target_node_name=node1_name, target_parameter_name='message', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='severity', target_node_name=node1_name, target_parameter_name='severity', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node1_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='severity', target_node_name=node2_name, target_parameter_name='severity', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='message', target_node_name=node2_name, target_parameter_name='message', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='message', node_name=node0_name, value=decode_value(top_level_unique_values_dict['0328987e655ccda6e67c8fc15e75e624']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='severity', node_name=node0_name, value=decode_value(top_level_unique_values_dict['f717e7d817dbc0e03438173773012fc4']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='fail_node_on_error', node_name=node0_name, value=decode_value(top_level_unique_values_dict['b5bea41b6c623f7c09f1bf24dcae58eb']), initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='severity', node_name=node1_name, value=decode_value(top_level_unique_values_dict['f717e7d817dbc0e03438173773012fc4']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='message', node_name=node1_name, value=decode_value(top_level_unique_values_dict['0328987e655ccda6e67c8fc15e75e624']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output', node_name=node1_name, value=decode_value(top_level_unique_values_dict['6f51c458d9fa5d13a394f9d3e673cb6e']), initial_setup=True, is_output=True))
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='exec_in', node_name=node2_name, value=decode_value(top_level_unique_values_dict['13d5bb126f2602fdfac6dceeb7c847be']), initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node2_name, value=decode_value(top_level_unique_values_dict['b5bea41b6c623f7c09f1bf24dcae58eb']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node2_name, value=decode_value(top_level_unique_values_dict['b5bea41b6c623f7c09f1bf24dcae58eb']), initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='result_details', node_name=node2_name, value=decode_value(top_level_unique_values_dict['eec80c33d01a30822ada8a44d78f23c2']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='result_details', node_name=node2_name, value=decode_value(top_level_unique_values_dict['eec80c33d01a30822ada8a44d78f23c2']), initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='severity', node_name=node2_name, value=decode_value(top_level_unique_values_dict['f717e7d817dbc0e03438173773012fc4']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='message', node_name=node2_name, value=decode_value(top_level_unique_values_dict['0328987e655ccda6e67c8fc15e75e624']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='message', node_name=node2_name, value=decode_value(top_level_unique_values_dict['0328987e655ccda6e67c8fc15e75e624']), initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='fail_node_on_error', node_name=node2_name, value=decode_value(top_level_unique_values_dict['b5bea41b6c623f7c09f1bf24dcae58eb']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='fail_node_on_error', node_name=node2_name, value=decode_value(top_level_unique_values_dict['b5bea41b6c623f7c09f1bf24dcae58eb']), initial_setup=True, is_output=True))

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
    parser.add_argument('--message', dest='message', default=None, help='New parameter')
    parser.add_argument('--severity', dest='severity', default=None, help='New parameter')
    parser.add_argument('--fail_node_on_error', dest='fail_node_on_error', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.message is not None:
            flow_input['Start Flow']['message'] = args.message
        if args.severity is not None:
            flow_input['Start Flow']['severity'] = args.severity
        if args.fail_node_on_error is not None:
            flow_input['Start Flow']['fail_node_on_error'] = args.fail_node_on_error
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
