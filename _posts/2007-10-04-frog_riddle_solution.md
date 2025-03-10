---
id: 68
title: "חידת צפרדע - הפתרון"
date: 2007-10-04 22:26:17
layout: post
categories: 
  - משחקים וחידות מתמטיות
---
החידה שהצגתי <a href="http://www.gadial.net/2007/09/29/frog_riddle/">בפוסט הקודם</a> עוררה קשיים שלא חשבתי שיתעוררו, דווקא בנקודה שנראתה לי (בטעות) שולית יחסית. לכן אנסה לכתוב כאן פתרון עבורה, למרות שכבר מספר קוראים עשו זאת היטב בתגובות לחידה עצמה.

אז מה היה לנו? צפרדע שמתחילה לנוע מהנקודה x ונעה k צעדים ימינה בכל צעד, כאשר x,k שניהם מספרים טבעיים. האבחנה הראשונה, ולטעמי החשובה והמרכזית בחידה, היא ששני הפרמטרים הללו - x,k - מאפיינים בצורה יחידה את המסלול שתעבור הצפרדע. אם אנחנו יודעים מהם, אנחנו יכולים לדעת איפה תהיה הצפרדע בכל רגע נתון.

זהו למעשה מקרה פרטי של מושג כללי יותר מ<a href="http://he.wikipedia.org/wiki/%D7%A7%D7%99%D7%A0%D7%9E%D7%98%D7%99%D7%A7%D7%94">קינמטיקה</a> בסיסית - תנועה במהירות קבועה. גם תנועה במהירות קבועה מאופיינת על ידי שני פרמטרים: המיקום בעת תחילת התנועה, ומהירות התנועה. כאן x הוא המיקום ו-k הוא המהירות. משוואת התנועה במקרה זה היא {% equation %}f(t)=x+kt{% endequation %} - כלומר, המיקום של הצפרדע בזמן t (כאשר t יכול לקבל רק ערכים טבעיים - הוא בעצם סופר את מספר הצעדים של הצפרדע) שווה למיקום ההתחלתי של הצפרדע ועוד המרחק שהספיקה לעבור (אם היא ביצעה צעד אחד, היא נעה k מספרים ימינה על הציר; אם היא ביצעה שני צעדים הרי שהיא זזה 2k צעדים וכן הלאה).

מכאן עולה שיטת ההתמודדות שלנו עם בעיית הצפרדע: בכל סיבוב "ננחש" ערכים אחרים עבור x,k. אם נזכור כמה נסיונות כושלים היו לנו עד עכשיו - כלומר, מהו t - נוכל לבדוק במדוייק עבור אותם ערכים של x,k האם צדקנו (כלומר, נבצע בדיקה במספר x+kt). בפסאודו קוד הדבר יראה ככה:
<ul>
	<li>    t=0</li>
	<li>לכל (x,k) בצע:
<ul>
	<li>t=t+1</li>
</ul>
<ul>
	<li>אם הצפרדע נמצאת ב-x+kt, החזר "ניצחתי!"</li>
</ul>
</li>
</ul>
<p dir="rtl" align="right">יש רק בעיה אחת בקוד הזה - בעיה שלי, כאמור, נראתה שולית יחסית, והתברר שטעיתי בחושבי שכך גם יחשבו הפותרים האחרים - לא ברור איך עוברים על כל ה-x,k האפשריים. במילים אחרות - איך לעבור בצורה סדרתית על כל הזוגות של מספרים טבעיים?</p>
<p dir="rtl" align="right">כדי להיווכח שגישה נאיבית לא תעבוד, בואו נחשוב מה יקרה אם נשאיר את x קבוע ושווה ל-1 ונגדיל את k כל הזמן. מכיוון ש-k יכול לקבל כל ערך טבעי, גדול ככל שיהיה, אף פעם לא "נגיע לסוף" הערכים ש-k יכול לקבל, ולכן אף פעם לא נעבור למקרה של x=2. לכן הדרך הזו נידונה לכישלון. דרך נכונה אפשרית אחת הראיתי ב<a href="http://www.gadial.net/2007/08/25/cantor_cardinality/">פוסט קודם</a>, כאשר הראיתי שהרציונליים הם בני מניה: לעבור על הזוגות על פי <strong>סכומם</strong>. כלומר, להתחיל מהזוג (1,1) כי הוא היחיד שסכומו 2, לעבור לזוגות (1,2) ו-(2,1), כי הם היחידים שסכומם 3, וכן הלאה. בשיטה הזו מובטח שנעבור על כל הזוגות. הנה פסאודו קוד שעושה משהו שכזה:</p>

<ul>
	<li>לכל i בתחום{1..} בצע:
<ul>
	<li>לכל j בתחום {1...i-1} בצע:
<ul>
	<li>עשה משהו על (j,i-j).</li>
</ul>
</li>
</ul>
</li>
</ul>
<p dir="rtl" align="right"> כאן i רץ על כל הסכומים האפשריים, ואילו j, לכל סכום, מאפשר לעבור באופן סדרתי על האיברים שנותנים סכום זה.</p>
<p dir="rtl" align="right">כמובן, אין צורך בגישה כל כך קפדנית ומדוייקת; לטעמי, די לומר "ידוע שאוסף כל הזוגות של הטבעיים הוא בן מניה ולכן ניתן לעבור עליו בצורה סדרתית" וזהו. אחת מהנקודות החשובות ב<a href="http://www.gadial.net/2007/09/15/what_is_algorithm/">פוסטים</a> <a href="http://www.gadial.net/2007/09/18/r_and_re/">הקודמים</a> שלי שדיברו על חישוביות היא שניתן לייצג כל קבוצה בת מניה באמצעות מספרים טבעיים - ולכן גם לעבור סדרתית על כל איבריה. זו נקודה חשובה ביותר, ואני מקווה שחידת הצפרדע מסייעת לראות זאת.</p>
<p dir="rtl" align="right">לסיום, "הרחבה" קטנה של החידה: נניח שאנחנו לא יכולים לבדוק את הצפרדע בכל סיבוב, אלא רק פעם בשישים סיבובים ("פעם בשעה") - האם זה משנה משהו? התשובה היא שכמובן שלא, ואשאיר זאת כאתגר עבורכם לראות מה התיקון (הקטן מאוד) שצריך לבצע בפתרון הנוכחי כדי לפתור גם את הבעיה הזו ואת כל הוריאציות הדומות לה.</p>
