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
    var state = document.querySelector(".footer-list")
    state.replaceChildren();
    for (const el of sections) {
      var check = document.createElement("div");

      if (i == avancement)
      {
        el.style.display = 'block';
        check.className = "footer-circle started";
      }
      else if (i > avancement)
      {
        el.style.display = 'none';
        check.className = "footer-circle";
      }
      else
      {
        el.style.display = 'none';
        check.className = "footer-circle ended";
      }

      state.appendChild(check)   
      i += 1
    }

    localStorage.setItem('index', JSON.stringify(avancement));
  }

  function addBtn(sections) {
    var next = document.querySelector(".next-button")
    next.addEventListener('click', function() { divide(sections, JSON.parse(localStorage.getItem('index')) - 1) });
    var prev = document.querySelector(".prev-button")
    prev.addEventListener('click', function() { divide(sections, JSON.parse(localStorage.getItem('index')) + 1) });

  }

  var sectionBlock = document.querySelectorAll('[id^=section]');

  divide(sectionBlock, 0)
  addBtn(sectionBlock)
})();