(function() {
  'use strict';

  function flashCopyMessage(el, msg) {
    el.textContent = msg;
    setTimeout(function() {
      el.textContent = "Copier";
    }, 1000);
  }

  function selectText(node) {
    var selection = window.getSelection();
    var range = document.createRange();
    range.selectNodeContents(node);
    selection.removeAllRanges();
    selection.addRange(range);
    return selection;
  }

  function addCopyButton(containerEl) {
    var copyBtn = document.createElement("button");
    copyBtn.className = "copy-button";
    copyBtn.textContent = "Copier";

    var codeEl = containerEl.querySelector(".language-python");
    copyBtn.addEventListener('click', function() {
      var selection = selectText(codeEl);
      navigator.clipboard.writeText(selectText(codeEl)).then(
        function(){
          selection.removeAllRanges();
          flashCopyMessage(copyBtn, 'Copié !')
        })
      .catch(
         function() {
          console && console.log(e);
          flashCopyMessage(copyBtn, 'Raté :\'(')
        });
    });

    containerEl.appendChild(copyBtn);
  }

  // Add copy button to code blocks
  var highlightBlocks = document.querySelectorAll('.code:not(.text)');

  Array.prototype.forEach.call(highlightBlocks, addCopyButton);
})();