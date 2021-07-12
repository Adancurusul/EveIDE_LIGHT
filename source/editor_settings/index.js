var bridge = null;
var editor = null;

require.config({ paths: { 'vs': './package/min/vs' } });
require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('container'), {
        fontFamily: "Verdana",
    });
    editor.onDidChangeModelContent((event) => {
        sendToPython("value", editor.getModel().getValue())
    })
    editor.onDidChangeModelLanguage((event) => {
        sendToPython("language", event.newLanguage)
    })
});

function init() {
    sendToPython("value", editor.getModel().getValue());
    sendToPython("language", editor.getModel()._languageIdentifier.language);
    sendToPython("theme", editor._themeService._theme.themeName);
}

function sendToPython(name, value) {
    bridge.receive_from_js(name, JSON.stringify(value));
}

function updateFromPython(name, value) {
    var data = JSON.parse(value)
    switch (name) {
        case "value":
            editor.getModel().setValue(data);
            break;
        case "language":
            monaco.editor.setModelLanguage(editor.getModel(), data);
            break;
        case "theme":
            monaco.editor.setTheme(data);
            sendToPython("theme", editor._themeService._theme.themeName);
            break;
    }
}

window.onload = function () {
    new QWebChannel(qt.webChannelTransport, function (channel) {
        bridge = channel.objects.bridge;
        bridge.sendDataChanged.connect(updateFromPython);
        bridge.init();
        init();
    });
}