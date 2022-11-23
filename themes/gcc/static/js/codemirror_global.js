// An "enum" of all code block types.
const LANGS = {
    PYTHON: "python",
    HTML: "html",
};

// Hold a reference to all the codeblocks.
// Will be filled at "compilation" time to register all the code blocks
var codeBlocks = {};

/// Exported function to add entries to codeBlocks.
function addBlock(name, content) {
    if (name in codeBlocks) {
        console.warn("Code block with name '" + name + "' already exists");
        return;
    }
    codeBlocks[name] = content;
}

function runIt(lang, number) {
    const nbstr = number.toString();

    console.log("Fetching codeBlock: " + lang + nbstr);
    var codeIO = codeBlocks[lang + nbstr];

    if (lang == LANGS.PYTHON) {
        console.log("Running codepython #" + nbstr);
        runItPython(codeIO);
    } else if (lang == LANGS.HTML) {
        console.log("Running codehtml #" + nbstr);
        runItHtml(codeIO);
    }
}

exports = {
    LANGS,
    addBlock,
    runIt,
};

// ============================== Python related ===============================

//// Skulpt
// Dict with external libs and init.js source code
var externalLibs = {};

function builtinRead(x) {
    if (externalLibs[x] !== undefined) {
        return Sk.misceval.promiseToSuspension(
            fetch(externalLibs[x]).then(function (resp) {
                return resp.text();
            })
        );
    }

    if (
        Sk.builtinFiles === undefined ||
        Sk.builtinFiles["files"][x] === undefined
    )
        throw "File not found: '" + x + "'";

    return Sk.builtinFiles["files"][x];
}

// Run the python code contained in codeIn and
// prints the output or the error on codeOut.
function runItPython(codeIO) {
    const [codeIn, codeOut, canvas] = codeIO;

    var prog = codeIn.getValue();
    codeOut.innerHTML = "";
    Sk.pre = "output";

    Sk.configure({
        // Output appends on the "codeOut" html element.
        output: function (text) {
            codeOut.innerHTML = codeOut.innerHTML + text;
        },
        read: builtinRead,
    });

    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = canvas;
    var myPromise = Sk.misceval.asyncToPromise(function () {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(
        function (mod) {
            console.log("success");
        },
        function (err) {
            console.log("failed");
            codeOut.innerText = err.toString();
        }
    );
}

// =============================== HTML related ================================

// Render the html contained in codeIn to codeOut
function runItHtml(codeIO) {
    const [codeIn, codeOut] = codeIO;
    var prog = codeIn.getValue();
    var out = codeOut.contentWindow.document;
    out.open();
    out.write("<!DOCTYPE html>"); // Added to shut up the "Quirks" warning.
    out.write(prog);
    out.close();
}
