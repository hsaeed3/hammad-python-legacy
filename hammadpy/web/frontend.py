#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadDash =================================================================#

from hammadpy import HammadPy
from dash import Dash, html, dcc
from typing import List, Dict, Optional, Union

#==============================================================================#

class UIBlocks:
    Div = html.Div
    Graph = dcc.Graph
    H1 = html.H1
    H2 = html.H2
    H3 = html.H3
    H4 = html.H4
    H5 = html.H5
    H6 = html.H6
    Dropdown = dcc.Dropdown
    Slider = dcc.Slider
    Checklist = dcc.Checklist
    RadioItems = dcc.RadioItems
    DatePickerSingle = dcc.DatePickerSingle
    DatePickerRange = dcc.DatePickerRange
    Input = dcc.Input
    Textarea = dcc.Textarea
    Upload = dcc.Upload
    Button = html.Button
    Img = html.Img
    Label = html.Label
    Link = html.A
    List = html.Ul
    ListItem = html.Li
    Table = html.Table
    TableCell = html.Td
    TableHeader = html.Th
    TableRow = html.Tr
    IFrame = html.Iframe
    Video = html.Video
    Audio = html.Audio
    Progress = html.Progress
    Marquee = html.Marquee
    Interval = dcc.Interval
    Location = dcc.Location
    Tabs = dcc.Tabs
    Tab = dcc.Tab
    Markdown = dcc.Markdown
    Badge = html.Span  
    Breadcrumb = html.Nav  
    Card = html.Div  
    Collapse = html.Div 
    Modal = html.Div 
    Tooltip = html.Div 
    Spinner = html.Div  
    Alert = html.Div 
    Accordion = html.Div  
    ConfirmDialog = dcc.ConfirmDialog 
    ConfirmDialogProvider = dcc.ConfirmDialogProvider 
    Store = dcc.Store

#==============================================================================#

class UI:
    def __init__(self, title: Optional[str] = "Hammad's Interactive Dash", debug: bool = False):
        """
        Initializes the UI application.

        Args:
            title (Optional[str]): Title of the Dash application, with a default value.
            debug (bool): Whether to run the app in debug mode.
        """
        self.hpy = HammadPy()
        self.title = title
        self.debug = debug
        self.app = Dash(__name__)
        self.blocks = []
        self._setup_layout()

    def _setup_layout(self):
        """
        Sets up the initial layout of the Dash application.
        """
        self.app.layout = html.Div([
            html.H1(children=self.title, style={'textAlign': 'center'}),
            html.Div(id='dynamic-column', children=[self._render_block(block) for block in self.blocks])
        ])

    def _render_block(self, block):
        """
        Renders individual blocks into Dash components.
        """
        return block

    def add_block(self, block: Union[UIBlocks.Div, UIBlocks.Graph, UIBlocks.H1, UIBlocks.H2, UIBlocks.H3, UIBlocks.H4, UIBlocks.H5, UIBlocks.H6, UIBlocks.Dropdown, UIBlocks.Slider, UIBlocks.Checklist, UIBlocks.RadioItems, UIBlocks.DatePickerSingle, UIBlocks.DatePickerRange, UIBlocks.Input, UIBlocks.Textarea, UIBlocks.Upload, UIBlocks.Button, UIBlocks.Img, UIBlocks.Label, UIBlocks.Link, UIBlocks.List, UIBlocks.ListItem, UIBlocks.Table, UIBlocks.TableCell, UIBlocks.TableHeader, UIBlocks.TableRow, UIBlocks.IFrame, UIBlocks.Video, UIBlocks.Audio, UIBlocks.Progress, UIBlocks.Marquee, UIBlocks.Interval, UIBlocks.Location, UIBlocks.Tabs, UIBlocks.Tab, UIBlocks.Markdown, UIBlocks.Badge, UIBlocks.Breadcrumb, UIBlocks.Card, UIBlocks.Collapse, UIBlocks.Modal, UIBlocks.Tooltip, UIBlocks.Spinner, UIBlocks.Alert, UIBlocks.Accordion, UIBlocks.ConfirmDialog, UIBlocks.ConfirmDialogProvider, UIBlocks.Store]):
        """
        Adds a new block to the Dash layout. The block can be any supported Dash component from the UIBlocks class.

        Args:
            block (Union[UIBlocks.*]): A Dash component to be added to the layout. Supported components include Div, Graph, H1-H6, Dropdown, Slider, Checklist, RadioItems, DatePickerSingle, DatePickerRange, Input, Textarea, Upload, Button, Img, Label, Link, List, ListItem, Table, TableCell, TableHeader, TableRow, IFrame, Video, Audio, Progress, Marquee, Interval, Location, Tabs, Tab, Markdown, ColorPicker, Badge, Breadcrumb, Card, Collapse, Modal, Tooltip, Spinner, Alert, Accordion, ConfirmDialog, ConfirmDialogProvider, Store.

        Example usage:
            ui.add_block(UIBlocks.Button("Click me"))
            ui.add_block(UIBlocks.Graph(figure=my_figure))
        """
        self.blocks.append(block)
        self._update_layout()

    def remove_block(self, index):
        """
        Removes a block from the Dash layout by index.
        """
        if 0 <= index < len(self.blocks):
            del self.blocks[index]
            self._update_layout()
        else:
            self.hpy.say("Invalid block index.", "red", "bold")

    def list_blocks(self) -> List:
        """
        Lists all blocks in the Dash layout.
        """
        return self.blocks

    def _update_layout(self):
        """
        Updates the layout of the Dash application to reflect changes in blocks.
        """
        self.app.layout.children[1].children = [self._render_block(block) for block in self.blocks]

    def run(self):
        """
        Runs the Dash app.
        """
        self.hpy.say("Starting HammadDash app...", "lightblack", "dim")
        self.app.run_server(debug=self.debug)

#==============================================================================#

if __name__ == '__main__':
    hammad_dash = UI(debug=True) 
    hammad_dash.add_block(html.P("This is a text paragraph.")) 
    hammad_dash.run()

#==============================================================================#
