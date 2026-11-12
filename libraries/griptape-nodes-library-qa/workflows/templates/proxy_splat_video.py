# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "proxy_Splat_Video"
# schema_version = "0.21.0"
# engine_version_created_with = "0.105.0"
# node_libraries_referenced = [["Griptape Nodes Library", "0.88.0"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "StartFlow"], ["Griptape Nodes Library", "WorldLabsWorldGeneration"]]
# description = "Gens a splat from video"
# is_griptape_provided = false
# is_template = true
# is_internal = false
# creation_date = 2026-10-16T11:23:09.124413Z
# last_modified_date = 2026-10-16T11:28:34.875397Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"text_prompt\":{\"name\":\"text_prompt\",\"tooltip\":\"Text description of the 3D world to generate\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Text Prompt\",\"multiline\":true,\"placeholder_text\":\"Describe the 3D world you want to generate...\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"model\":{\"name\":\"model\",\"tooltip\":\"Marble model\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"marble-1.1\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Model\",\"simple_dropdown\":[\"marble-1.1-plus\",\"marble-1.1\",\"marble-1.0\",\"marble-1.0-draft\"]},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"randomize_seed\":{\"name\":\"randomize_seed\",\"tooltip\":\"New parameter\",\"type\":\"bool\",\"input_types\":[\"any\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"seed\":{\"name\":\"seed\",\"tooltip\":\"New parameter\",\"type\":\"int\",\"input_types\":[\"any\"],\"output_type\":\"int\",\"default_value\":42,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"video\":{\"name\":\"video\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"VideoUrlArtifact\",\"VideoArtifact\",\"str\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Video Input\",\"hide\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"splat_100k\":{\"name\":\"splat_100k\",\"tooltip\":\"100k resolution Gaussian splat\",\"type\":\"SplatUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"SplatUrlArtifact\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Splat (100k)\",\"pulse_on_run\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"splat_500k\":{\"name\":\"splat_500k\",\"tooltip\":\"500k resolution Gaussian splat\",\"type\":\"SplatUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"SplatUrlArtifact\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Splat (500k)\",\"pulse_on_run\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"splat_full_res\":{\"name\":\"splat_full_res\",\"tooltip\":\"Full resolution Gaussian splat\",\"type\":\"SplatUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"SplatUrlArtifact\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Splat (Full Res)\",\"pulse_on_run\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"mesh\":{\"name\":\"mesh\",\"tooltip\":\"Collider mesh (GLB)\",\"type\":\"ThreeDUrlArtifact\",\"input_types\":[\"any\"],\"output_type\":\"ThreeDUrlArtifact\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"display_name\":\"Mesh (GLB)\",\"pulse_on_run\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null}}}}"
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
    context_manager = GriptapeNodes.ContextManager()
    if not context_manager.has_current_workflow():
        context_manager.push_workflow(file_path=__file__)
    # Every unique parameter value, stored once and keyed by a hash of its content.
    # Values that aren't plain data carry a '$type' naming their class; decode_value rebuilds them.
    top_level_unique_values_dict = {'fcbcf165908dd18a9e49f7ff27810176': False, '284b7e6d788f363f910f7beb1910473e': 600, '73c551d17e8c2222d8bcff87f94676e8': 'marble-1.1', '72bcb013ed85a48ff6da50bc18d37492': 'Video', '12ae32cb1ec02d01eda3581b127c1fee': '', '643d5437104296e21d906ecb15b2c96a': [[], []], '4f53cda18c2baa0c0354bb5f9a3ecbe5': [], '73475cb40a568e8da8a045ced110137e': 42, 'b65175eed17daf44276676633cd507d6': 'splat_full_res.spz'}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='WorldLabsWorldGeneration', specific_library_name='Griptape Nodes Library', node_name='World Labs World Generation', metadata={'position': {'x': 650, 'y': 0}, 'tempId': 'placing-1792149797055-lnq80b', 'library_node_metadata': {'category': 'Splat', 'description': 'Generate 3D worlds using World Labs Marble via Griptape model proxy', 'display_name': 'World Labs World Generation', 'tags': ['splat', '3d', 'generation', 'ai', 'api', 'world-labs'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [{'type': 'model_usage', 'model_ids': ['gtc_marble_1_1_plus', 'gtc_marble_1_1', 'gtc_marble_1_0', 'gtc_marble_1_0_draft']}]}, 'library': 'Griptape Nodes Library', 'node_type': 'WorldLabsWorldGeneration', 'showaddparameter': False, 'size': {'width': 600, 'height': 1996}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='images_ParameterListUniqueParamID_45e11e7bf3d047a988d6d6994493870e', default_value=[], tooltip='Multiple images for multi-view world generation (2-8 images)', type='ImageArtifact', input_types=['ImageArtifact', 'ImageUrlArtifact', 'str', 'list', 'list[ImageArtifact]', 'list[ImageUrlArtifact]'], output_type='ImageArtifact', ui_options={'expander': True, 'display_name': 'Images', 'hide': False}, mode_allowed_output=False, parent_container_name='images', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='images_ParameterListUniqueParamID_e9f409a7ee2849cb90b2418e9f37aa77', default_value=[], tooltip='Multiple images for multi-view world generation (2-8 images)', type='ImageArtifact', input_types=['ImageArtifact', 'ImageUrlArtifact', 'str', 'list', 'list[ImageArtifact]', 'list[ImageUrlArtifact]'], output_type='ImageArtifact', ui_options={'expander': True, 'display_name': 'Images', 'hide': False}, mode_allowed_output=False, parent_container_name='images', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='video', ui_options={'display_name': 'Video Input', 'hide': False}, initial_setup=True))
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='disable_recaption', ui_options={'display_name': 'Disable Auto-Recaption', 'hide': False, 'hide_label': False, 'hide_property': False}, initial_setup=True))
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'position': {'x': -301.58708189158017, 'y': 151.94463667820068}, 'size': {'width': 600, 'height': 986}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='text_prompt', default_value='', tooltip='Text description of the 3D world to generate', type='str', input_types=['any'], output_type='str', ui_options={'display_name': 'Text Prompt', 'multiline': True, 'placeholder_text': 'Describe the 3D world you want to generate...'}, traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='model', default_value='marble-1.1', tooltip='Marble model', type='str', input_types=['any'], output_type='str', ui_options={'display_name': 'Model', 'simple_dropdown': ['marble-1.1-plus', 'marble-1.1', 'marble-1.0', 'marble-1.0-draft']}, traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='randomize_seed', default_value=False, tooltip='New parameter', type='bool', input_types=['any'], output_type='bool', ui_options={'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='seed', default_value=42, tooltip='New parameter', type='int', input_types=['any'], output_type='int', ui_options={'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['VideoUrlArtifact', 'VideoArtifact', 'str'], output_type='VideoUrlArtifact', ui_options={'display_name': 'Video Input', 'hide': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', traits=[], initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'position': {'x': 1590.076124567474, 'y': 151.94463667820068}, 'size': {'width': 600, 'height': 996}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='splat_100k', tooltip='100k resolution Gaussian splat', type='SplatUrlArtifact', input_types=['any'], output_type='SplatUrlArtifact', ui_options={'display_name': 'Splat (100k)', 'pulse_on_run': True}, traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='splat_500k', tooltip='500k resolution Gaussian splat', type='SplatUrlArtifact', input_types=['any'], output_type='SplatUrlArtifact', ui_options={'display_name': 'Splat (500k)', 'pulse_on_run': True}, traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='splat_full_res', tooltip='Full resolution Gaussian splat', type='SplatUrlArtifact', input_types=['any'], output_type='SplatUrlArtifact', ui_options={'display_name': 'Splat (Full Res)', 'pulse_on_run': True}, traits=[], initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='mesh', tooltip='Collider mesh (GLB)', type='ThreeDUrlArtifact', input_types=['any'], output_type='ThreeDUrlArtifact', ui_options={'display_name': 'Mesh (GLB)', 'pulse_on_run': True}, traits=[], initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='exec_out', target_node_name=node0_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='model', target_node_name=node0_name, target_parameter_name='model', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='splat_100k', target_node_name=node2_name, target_parameter_name='splat_100k', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='splat_500k', target_node_name=node2_name, target_parameter_name='splat_500k', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='splat_full_res', target_node_name=node2_name, target_parameter_name='splat_full_res', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='mesh', target_node_name=node2_name, target_parameter_name='mesh', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='failure', target_node_name=node2_name, target_parameter_name='failed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='randomize_seed', target_node_name=node0_name, target_parameter_name='randomize_seed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='seed', target_node_name=node0_name, target_parameter_name='seed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='video', target_node_name=node0_name, target_parameter_name='video', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='api_key_provider', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='timeout', node_name=node0_name, value=decode_value(top_level_unique_values_dict['284b7e6d788f363f910f7beb1910473e']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node0_name, value=decode_value(top_level_unique_values_dict['73c551d17e8c2222d8bcff87f94676e8']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='input_type', node_name=node0_name, value=decode_value(top_level_unique_values_dict['72bcb013ed85a48ff6da50bc18d37492']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='text_prompt', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='is_panorama', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='images', node_name=node0_name, value=decode_value(top_level_unique_values_dict['643d5437104296e21d906ecb15b2c96a']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='images_ParameterListUniqueParamID_45e11e7bf3d047a988d6d6994493870e', node_name=node0_name, value=decode_value(top_level_unique_values_dict['4f53cda18c2baa0c0354bb5f9a3ecbe5']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='images_ParameterListUniqueParamID_e9f409a7ee2849cb90b2418e9f37aa77', node_name=node0_name, value=decode_value(top_level_unique_values_dict['4f53cda18c2baa0c0354bb5f9a3ecbe5']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='azimuth_angles', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='enable_reconstruction', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='disable_recaption', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='display_name', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='tags', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='randomize_seed', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='seed', node_name=node0_name, value=decode_value(top_level_unique_values_dict['73475cb40a568e8da8a045ced110137e']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node0_name, value=decode_value(top_level_unique_values_dict['b65175eed17daf44276676633cd507d6']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='text_prompt', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node1_name, value=decode_value(top_level_unique_values_dict['73c551d17e8c2222d8bcff87f94676e8']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='randomize_seed', node_name=node1_name, value=decode_value(top_level_unique_values_dict['fcbcf165908dd18a9e49f7ff27810176']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='seed', node_name=node1_name, value=decode_value(top_level_unique_values_dict['73475cb40a568e8da8a045ced110137e']), initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='video', node_name=node1_name, value=decode_value(top_level_unique_values_dict['12ae32cb1ec02d01eda3581b127c1fee']), initial_setup=True, is_output=False))
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
    parser.add_argument('--text_prompt', dest='text_prompt', default=None, help='Text description of the 3D world to generate')
    parser.add_argument('--model', dest='model', default=None, help='Marble model')
    parser.add_argument('--randomize_seed', dest='randomize_seed', default=None, help='New parameter')
    parser.add_argument('--seed', dest='seed', default=None, help='New parameter')
    parser.add_argument('--video', dest='video', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.text_prompt is not None:
            flow_input['Start Flow']['text_prompt'] = args.text_prompt
        if args.model is not None:
            flow_input['Start Flow']['model'] = args.model
        if args.randomize_seed is not None:
            flow_input['Start Flow']['randomize_seed'] = args.randomize_seed
        if args.seed is not None:
            flow_input['Start Flow']['seed'] = args.seed
        if args.video is not None:
            flow_input['Start Flow']['video'] = args.video
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
