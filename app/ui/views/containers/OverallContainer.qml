import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Rectangle {
    id: overall_container
    Layout.preferredWidth: parent.width * 0.95
    Layout.fillHeight: true

    ColumnLayout {
        anchors.fill: parent
        spacing: 2

        Rectangle {
            id: performance
            color: "#C2C2C2"
            Layout.fillWidth: true
            Layout.preferredHeight: parent.height * 0.7
        }

        Rectangle {
            id: processes
            color: "#C2C2C2"
            Layout.fillWidth: true
            Layout.preferredHeight: parent.height * 0.3

        }
    }
}