"use strict";(self.webpackChunk_splunk_ucc_ui_lib=self.webpackChunk_splunk_ucc_ui_lib||[]).push([[556],{17556:(e,t,n)=>{n.r(t),n.d(t,{default:()=>ee});var r=n(67294),a=n(36219),o=n(62672),l=n.n(o),i=n(41946),c=n.n(i),u=n(71569),f=n.n(u),s=n(12788),m=n(54418),p=n(64255),b=n(71263),y=n(46054),d=n(45697),v=n.n(d),g=n(13685);function h(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function O(e){var t,n,o=e.tab,l=(t=(0,r.useState)(!0),n=2,function(e){if(Array.isArray(e))return e}(t)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,a,o,l,i=[],c=!0,u=!1;try{if(o=(n=n.call(e)).next,0===t){if(Object(n)!==n)return;c=!1}else for(;!(c=(r=o.call(n)).done)&&(i.push(r.value),i.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=n.return&&(l=n.return(),Object(l)!==l))return}finally{if(u)throw a}}return i}}(t,n)||function(e,t){if(e){if("string"==typeof e)return h(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?h(e,t):void 0}}(t,n)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),i=l[0],c=l[1],u=(0,r.useRef)(null),f=(0,p.YK)().meta.name;return(0,r.useEffect)((function(){new Promise((function(e){"external"===o.customTab.type?import("".concat((0,g.a)(),"/custom/").concat(o.customTab.src,".js")).then((function(t){var n=t.default;e(n)})):require(["app/".concat(f,"/js/build/custom/").concat(o.customTab.src)],(function(t){return e(t)}))})).then((function(e){new e(o,u.current).render(),c(!1)}))}),[]),r.createElement(r.Fragment,null,i&&(0,a._)("Loading..."),r.createElement("div",{ref:u,style:{visibility:i?"hidden":"visible"}}))}O.propTypes={tab:v().object.isRequired};const j=O;var E,S=n(95414),w=n.n(S),A=n(3893),T=n(92246),k=n(12297),I=n(61435),P=n(56070),C=n(87228);function _(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,a,o,l,i=[],c=!0,u=!1;try{if(o=(n=n.call(e)).next,0===t){if(Object(n)!==n)return;c=!1}else for(;!(c=(r=o.call(n)).done)&&(i.push(r.value),i.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=n.return&&(l=n.return(),Object(l)!==l))return}finally{if(u)throw a}}return i}}(e,t)||function(e,t){if(e){if("string"==typeof e)return N(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?N(e,t):void 0}}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function N(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}var x,R,z=s.default.div(E||(x=["\n    margin-left: 270px !important;\n    width: 150px;\n"],R||(R=x.slice(0)),E=Object.freeze(Object.defineProperties(x,{raw:{value:Object.freeze(R)}}))));function L(e){var t=e.serviceName,n=(0,r.useRef)(),o=_((0,r.useState)(null),2),l=o[0],i=o[1],c=_((0,r.useState)(!1),2),u=c[0],f=c[1],s=_((0,r.useState)({}),2),m=s[0],p=s[1];if((0,r.useEffect)((function(){(0,k.L)({serviceName:"settings/".concat(t),handleError:!0,callbackOnError:function(e){e.uccErrorCode="ERR0005",i(e)}}).then((function(e){p(e.data.entry[0].content)}))}),[t]),null!=l&&l.uccErrorCode)throw l;return Object.keys(m).length?r.createElement(r.Fragment,null,r.createElement(A.Z,{ref:n,page:C.y,stanzaName:t,serviceName:"settings",mode:I.DE,currentServiceState:m,handleFormSubmit:function(e){f(e)}}),r.createElement(z,null,r.createElement(T.Sn,{className:"saveBtn",appearance:"primary",label:u?r.createElement(w(),null):(0,a._)("Save"),onClick:function(){n.current.handleSubmit()},disabled:u}))):r.createElement(P.XE,{size:"medium"})}L.propTypes={serviceName:v().string.isRequired};const Z=L;var q=n(56057),D=n(54808),M=n(5792),U=n(63649),$=n(67475);function F(e){return F="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},F(e)}function K(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function Y(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?K(Object(n),!0).forEach((function(t){B(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):K(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function B(e,t,n){return(t=function(e){var t=function(e,t){if("object"!==F(e)||null===e)return e;var n=e[Symbol.toPrimitive];if(void 0!==n){var r=n.call(e,"string");if("object"!==F(r))return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"===F(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function G(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function W(e){var t,n,a=e.selectedTab,o=e.updateIsPageOpen,l=(t=(0,r.useState)({open:!1}),n=2,function(e){if(Array.isArray(e))return e}(t)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,a,o,l,i=[],c=!0,u=!1;try{if(o=(n=n.call(e)).next,0===t){if(Object(n)!==n)return;c=!1}else for(;!(c=(r=o.call(n)).done)&&(i.push(r.value),i.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=n.return&&(l=n.return(),Object(l)!==l))return}finally{if(u)throw a}}return i}}(t,n)||function(e,t){if(e){if("string"==typeof e)return G(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?G(e,t):void 0}}(t,n)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),i=l[0],c=l[1],u=a.style===$.G;(0,r.useEffect)((function(){u&&o(!!i.open)}),[i]);return r.createElement(q.W,{value:null},u&&i.open&&r.createElement(U.Z,{open:i.open,handleRequestClose:function(){c(Y(Y({},i),{},{open:!1}))},serviceName:a.name,stanzaName:i.stanzaName,mode:i.mode,formLabel:i.formLabel,page:C.y}),r.createElement("div",{style:u&&i.open?{display:"none"}:{display:"block"}},r.createElement(D.Z,{page:C.y,serviceName:a.name,handleRequestModalOpen:function(){c(Y(Y({},i),{},{open:!0,mode:I.jg,formLabel:"Add ".concat(a.title)}))},handleOpenPageStyleDialog:function(e,t){c(Y(Y({},i),{},{open:!0,stanzaName:e.name,formLabel:t===I.Oh?"Clone ".concat(a.title):"Update ".concat(a.title),mode:t}))}})),!u&&i.open&&r.createElement(M.Z,{page:C.y,open:i.open,handleRequestClose:function(){c(Y(Y({},i),{},{open:!1}))},serviceName:a.name,mode:I.jg,formLabel:i.formLabel}))}W.propTypes={selectedTab:v().object,updateIsPageOpen:v().func};const X=(0,r.memo)(W);var H;function J(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var n=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=n){var r,a,o,l,i=[],c=!0,u=!1;try{if(o=(n=n.call(e)).next,0===t){if(Object(n)!==n)return;c=!1}else for(;!(c=(r=o.call(n)).done)&&(i.push(r.value),i.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=n.return&&(l=n.return(),Object(l)!==l))return}finally{if(u)throw a}}return i}}(e,t)||function(e,t){if(e){if("string"==typeof e)return Q(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?Q(e,t):void 0}}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function Q(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}var V=(0,s.default)(f().Row)(H||(H=function(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}(["\n    padding: 5px 0px;\n\n    .dropdown {\n        text-align: right;\n    }\n\n    .input_button {\n        text-align: right;\n        margin-right: 0px;\n    }\n"])));const ee=function(){var e=(0,p.YK)().pages.configuration,t=e.title,n=e.description,o=e.tabs,i=o.map((function(e){return e.name})),u=J((0,r.useState)(o[0].name),2),s=u[0],d=u[1],v=J((0,r.useState)(!1),2),g=v[0],h=v[1],O=(0,m.Z)();(0,r.useEffect)((function(){O&&i.includes(O.get("tab"))&&O.get("tab")!==s&&d(O.get("tab"))}),[]);var E=(0,r.useCallback)((function(e,t){var n=t.selectedTabId;d(n),h(!1)}),[s]),S=function(e){h(e)};return r.createElement(y.Z,null,r.createElement("div",{style:g?{display:"none"}:{display:"block"}},r.createElement(f(),{gutter:8},r.createElement(V,null,r.createElement(f().Column,{span:9},r.createElement(b.r3,null,(0,a._)(t)),r.createElement(b.pZ,null,(0,a._)(n||""))))),r.createElement(l(),{activeTabId:s,onChange:E},o.map((function(e){return r.createElement(l().Tab,{key:e.name,label:(0,a._)(e.title),tabId:e.name})})))),o.map((function(e){return function(e){var t;return t=null!=e&&e.customTab?function(e){return r.createElement(j,{tab:e})}(e):null!=e&&e.table?r.createElement(X,{key:e.name,selectedTab:e,updateIsPageOpen:S}):r.createElement(Z,{key:e.name,serviceName:e.name}),r.createElement("div",{key:e.name,style:e.name!==s?{display:"none"}:{display:"block"},id:"".concat(e.name,"Tab")},t)}(e)})),r.createElement(c(),{position:"top-right"}))}}}]);
//# sourceMappingURL=556.js.map