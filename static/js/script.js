function copyText() {
  navigator.clipboard.writeText(document.getElementById("content").innerText);
  alert("복사 되었습니다!");
}

function copyHTML() {
  const element = document.getElementById("content");

  // 선택 영역을 만들기 위해 Range와 Selection 객체 사용
  const range = document.createRange();
  range.selectNodeContents(element);

  const selection = window.getSelection();
  selection.removeAllRanges(); // 기존 선택 영역 제거
  selection.addRange(range); // 새로운 선택 영역 추가

  // 복사 실행
  document.execCommand("copy");

  // 선택 영역 해제
  selection.removeAllRanges();
  alert("복사 되었습니다!");
}
