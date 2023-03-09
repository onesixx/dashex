from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_admin_components as dac

import model
import callbacks
import view

# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = Dash(__name__)
server = app.server

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([
    dac.Navbar(dac.NavbarDropdown(dac.NavbarDropdownItem())),
    dac.Sidebar(dac.SidebarMenu([dac.SidebarMenuItem(),  # id='tab_menu_a', label='A', icon='heart'),
                                 ]), title='TEST'),
    dac.Body(dac.TabItems(view.content)),
    dac.Controlbar(),
    dac.Footer()
])

# =============================================================================
# # Callback
# # =============================================================================
# @app.callback(
#       Output('tabitem_a_content', 'active'),
#       Input('tab_menu_a', 'n_clicks'))
# def display_tab(nClick):
#     return True,True#, (True,True)
callbacks.get_callbacks(app)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
