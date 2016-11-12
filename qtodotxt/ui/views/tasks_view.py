from PyQt5 import QtCore, QtWidgets, QtGui
from qtodotxt.ui.views.tasks_search_view import TasksSearchView
from qtodotxt.ui.views.tasks_list_view import TasksListView


class TasksView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(TasksView, self).__init__(parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.tasks_search_view = TasksSearchView(QtGui.QIcon(":/white_icons/resources/ActionSearch.png"),
                                                 QtGui.QIcon(":/white_icons/resources/ActionClear.png"), self)
        self.tasks_list_view = TasksListView(self)
        offset = QtCore.QSettings().value("ui_margin_offset", -4)
        self.setContentsMargins(2 * offset, offset, offset, offset)
        layout.addWidget(self.tasks_search_view)
        layout.addWidget(self.tasks_list_view)
        self.setLayout(layout)
