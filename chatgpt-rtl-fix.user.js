// ==UserScript==
// @name         ChatGPT Arabic RTL Fix
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  Forces RTL direction for Arabic text in ChatGPT
// @author       Amr
// @match        https://chatgpt.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 1. حقن تنسيقات CSS إجبارية (!important) لتخطي قيود واجهة ChatGPT
    const style = document.createElement('style');
    style.innerHTML = `
        [dir="rtl"] {
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: plaintext !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        }
        ul[dir="rtl"], ol[dir="rtl"] {
            padding-right: 1.5rem !important;
            padding-left: 0 !important;
        }
    `;
    document.head.appendChild(style);

    const arabicRegex = /[\u0600-\u06FF]/;

    function applyRTL() {
        // 2. استهداف جميع عناصر النصوص في الصفحة بدون الاعتماد على كلاس قديم
        const elements = document.querySelectorAll('p, li, h1, h2, h3, h4, ul, ol, strong, div[data-message-author-role] div');

        elements.forEach(el => {
            // تجاهل مربعات الأكواد البرمجية حتى لا تنعكس
            if (el.closest('pre, code')) return;

            const text = (el.innerText || el.textContent || '').trim();
            if (arabicRegex.test(text) && el.getAttribute('dir') !== 'rtl') {
                el.setAttribute('dir', 'rtl');
            }
        });
    }

    // التشغيل كل نصف ثانية لضبط النصوص فور ظهورها
    setInterval(applyRTL, 500);
})();
