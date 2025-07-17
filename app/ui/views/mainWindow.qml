import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "containers"
import "components"

ApplicationWindow {
    id: mainWindow
    width: 854
    height: 480
    visible: true
    title: "trackR"
    maximumWidth: 1920
    maximumHeight: 1080

    Rectangle {
        anchors.fill: parent
        color: "#FAF9F6"

        RowLayout {
            id: main_layout
            anchors.fill: parent
            anchors.margins: 10
            spacing: 4

            MenuContainer { }
            OverallContainer { }
        }
    }


    Connections {
        target: bridge
        function onData_updated(data) {
            // welcomeLabel.text = data.cpu.cpu_temp.toFixed(2)
        }
    }

    Timer {
        id: updateTimer
        interval: 1000 // Update every second
        running: true
        repeat: true
        onTriggered: bridge.update_data()
    }
}