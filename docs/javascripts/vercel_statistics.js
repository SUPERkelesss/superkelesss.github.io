// docs/js/vercel-analytics.js
window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };

// 动态加载 Vercel Analytics 脚本
(function() {
  var script = document.createElement('script');
  script.src = '/_vercel/insights/script.js';
  script.defer = true;
  document.head.appendChild(script);
})();