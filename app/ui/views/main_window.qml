import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: mainWindow
    width: 854
    height: 480
    visible: true
    title: "trackR"
    maximumWidth: 1920
    maximumHeight: 1080

    ColumnLayout {
        anchors.fill: parent

        Label {
            id: welcomeLabel
            text: "trackR"
            font.pointSize: 24
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
        }
    }

    Connections {
        target: bridge
        function onData_updated(data) {
            welcomeLabel.text = data.cpu.cpu_temp.toFixed(2)
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