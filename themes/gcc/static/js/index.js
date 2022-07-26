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


  if (localStorage.getItem("index") === null)
    localStorage.setItem('index', JSON.stringify(0))

  function divide(sections, avancement) {
    var i = 0
    for (const el of sections) {
      if (i == avancement)
        el.style.display = 'block';
      else
        el.style.display = 'none';
      i += 1
    }

    localStorage.setItem('index', JSON.stringify(avancement));
  }

  function addBtn(sections) {
    for (const el of sections) {
      var div = document.createElement("div");
      div.style = "display: flex; place-content: space-between;"

      var prevBtn = document.createElement("next");
      prevBtn.className = "copy-button";
      prevBtn.textContent = "Prev";
      prevBtn.addEventListener('click', function() { divide(sections, JSON.parse(localStorage.getItem('index')) - 1) });
      div.appendChild(prevBtn);

      var nextBtn = document.createElement("next");
      nextBtn.className = "copy-button";
      nextBtn.textContent = "Next";
      nextBtn.addEventListener('click', function() { divide(sections, JSON.parse(localStorage.getItem('index')) + 1) });
      div.appendChild(nextBtn);
      el.appendChild(div)
    }
  }

  var sectionBlock = document.querySelectorAll('[id^=section]');

  divide(sectionBlock, 0)
  addBtn(sectionBlock)
})();