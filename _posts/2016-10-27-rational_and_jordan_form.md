---
id: 3380
title: "צורת ז'ורדן והצורה הרציונלית - התיאוריה"
date: 2016-10-27 14:39:17
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - הצורה הרציונלית
  - משפט הפירוק הפרימרי
  - משפט הפירוק הציקלי
  - צורת ז'ורדן
---
<strong>הקדמה מרגשת</strong>

הפוסט הזה מיועד לסגור את שרשרת הפוסטים שלי על אלגברה לינארית שעוסקים בנושא של צורות קנוניות - וככזה, כמובן שלא יהיה ניתן להבין ממנו כמעט כלום בלי לקרוא את הפוסטים הקודמים או בלי להכיר אלגברה לינארית. בכל זאת, בואו נתחיל עם מבוא ידידותי שמזכיר לנו מה בעצם אנחנו עושים כאן ולמה. אני עדיין מניח שאתם מכירים אלגברה לינארית ברמת המה-זו-מטריצה ומה-זו-טרנספורמציה-לינארית.

הרעיון הבסיסי הוא שיש לנו מרחב וקטורי {% equation %}V{% endequation %} סוף-ממדי שמוגדרת מעליו טרנספורמציה לינארית {% equation %}T:V\to V{% endequation %} ("מעליו", כלומר מהמרחב לעצמו; כל הנושא של צורות קנוניות לא מתעסק בטרנספורמציות בין שני מרחבים שונים) ואנחנו מחפשים ל-{% equation %}V{% endequation %} בסיס שבו המטריצה שמייצגת את {% equation %}T{% endequation %} היא שני דברים: <strong>פשוטה</strong> ו<strong>קנונית</strong>. ל"פשוטה" אין הגדרה פורמלית כל כך - בפוסט הזה נראה שתי גישות שונות לעניין הזה - אבל "קנונית" זה משהו יותר ברור: זה אומר <strong>קיום ויחידות</strong>. מרגע שהחלטנו על סוג מסויים של צורה קנונית (למשל, צורת ז'ורדן), לכל טרנספורמציה {% equation %}T{% endequation %} תהיה <strong>קיימת</strong> מטריצה מייצגת ששייכת לצורה הזו, והמטריצה המייצגת הזו תהיה <strong>יחידה</strong> - לא יהיה לנו חופש בחירה בין כמה מטריצות מייצגות שונות.

הדבר דומה לפירוק היחיד למכפלת ראשוניים שיש למספרים טבעיים: אפשר לכתוב את 30 בתור כל מני מכפלות, למשל {% equation %}30=1\cdot30{% endequation %} או {% equation %}30=2\cdot15{% endequation %} או {% equation %}30=15\cdot2{% endequation %} וכדומה, אבל יש רק דרך אחת לכתוב אותו בתור מכפלה של מספרים שכולם ראשוניים (בפרט, 1 לא משתתף במכפלה כי הוא לא נחשב ראשוני) והראשוניים ממויינים לפי גודלם. כלומר, המכפלה היא {% equation %}30=2\cdot3\cdot5{% endequation %}. לכל מספר טבעי חיובי קיימת הצגה כזו (עבור 1 אומרים שזו "המכפלה הריקה").

אני מדבר כאן על טרנספורמציות לינאריות, אבל מכיוון שבאלגברה לינארית סוף-ממדית יש קשר הדוק בין טרנספורמציות לינאריות ומטריצות, אפשר לנסח את כל הדיון גם עבור מטריצות. אם {% equation %}A,B{% endequation %} מייצגות את הטרנספורמציה {% equation %}T{% endequation %} בבסיסים שונים אז פירוש הדבר הוא שקיימת מטריצה הפיכה {% equation %}P{% endequation %} כך ש-{% equation %}A=P^{-1}BP{% endequation %} ({% equation %}P{% endequation %} היא מטריצת מעבר בין הבסיסים; הרעיון הוא שבהינתן וקטור בבסיס של {% equation %}A{% endequation %}, {% equation %}P{% endequation %} מעבירה את הוקטור לבסיס של {% equation %}B{% endequation %}, ואז מפעילים את {% equation %}B{% endequation %}, ואז חוזרים עם {% equation %}P^{-1}{% endequation %} לבסיס של {% equation %}A{% endequation %}). על מטריצות {% equation %}A,B{% endequation %} כאלו שקיימת {% equation %}P{% endequation %} הפיכה כך ש-{% equation %}A=P^{-1}BP{% endequation %} אומרים שהן <strong>דומות</strong>. דמיון מטריצות כזה הוא <strong>יחס שקילות</strong> ולכן אפשר לדבר על נציגים קנוניים למחלקות השקילות, וחזרנו שוב לאותו סיפור. מכאן ואילך אני הולך לדבר על מטריצות ועל טרנספורמציות בצורה חופשית לחלוטין, לפי מה שנוח לי באותה שניה.

הדוגמה הבסיסית ביותר לצורה קנונית שרואים באלגברה לינארית היא <strong>מטריצה אלכסונית</strong>. הבעיה כאן היא שלא כל מטריצה דומה למטריצה אלכסונית - אנחנו מצמצמים מראש את הדיון ל<strong>מטריצות לכסינות</strong>. מה שברור מייד הוא שאם טרנספורמציה מיוצגת על ידי מטריצה אלכסונית, אז מה שנמצא על האלכסון של המטריצה ההיא הם <strong>הערכים העצמיים</strong> של הטרנספורמציה. כלומר, כל הסקלרים {% equation %}\lambda{% endequation %} כך שקיים וקטור {% equation %}v\ne0{% endequation %} עבורו {% equation %}Tv=\lambda v{% endequation %}. האבחנה הזו היא גם מה שהנחה את האופן שבו בודקים אם מטריצה היא לכסינה - מוצאים את הערכים העצמיים שלה, שהם השורשים של פולינום מסויים שנקרא <strong>הפולינום האופייני</strong> של המטריצה, ואז בודקים אם יש "מספיק" וקטורים עצמיים עבור הערכים העצמיים הללו - אם אנחנו מוצאים בסיס למרחב כולו שמורכב מוקטורים עצמיים. אם יש, גמרנו. אם אין, אפשר לשכוח מכך שהמטריצה תהיה דומה למטריצה אלכסונית.

ה"פתרון" לבעיה של "אין מספיק וקטורים עצמיים" הוא צורת ז'ורדן. צורת ז'ורדן היא מטריצה "כמעט-אלכסונית" - הערכים העצמיים עדיין יושבים על האלכסון הראשי, אבל באלכסון שמעליו יכולים להופיע פה ושם 1-ים. אם להיות יותר מדויקים, צורת ז'ורדן היא מטריצה <strong>בלוקים</strong>, כשכל בלוק הוא תת-מטריצה בעצמו שאנחנו "שותלים" על האלכסון הראשי. בלוק ז'ורדן שכזה בנוי ממטריצה סקלרית (כלומר, כזו שיש על האלכסון הראשי שלה ערך קבוע יחיד) ו-1-ים בכל האלכסון שמעל האלכסון הראשי. משהו כזה:

{% equation %}\left(\begin{array}{ccc}\lambda &amp; 1 &amp; 0\\0 &amp; \lambda &amp; 1\\0 &amp; 0 &amp; \lambda\end{array}\right){% endequation %}

זו דוגמה לבלוק ז'ורדן מגודל 3. על מטריצה אלכסונית אפשר לחשוב כאילו היא מורכבת כולה מבלוקי ז'ורדן מגודל 1, כך שצורת ז'ורדן מכלילה את הלכסון הרגיל. אם כן, האם הגענו אל המנוחה ואל הנחלה? כמעט. בשביל שלמטריצה כלשהי תהיה צורת ז'ורדן, צריך שכל הערכים העצמיים שלה <strong>יהיו בשדה שמעליו עובדים</strong>. מה זה אומר? קחו את הפולינום {% equation %}x^{2}+1{% endequation %} בתור דוגמה. השורשים של הפולינום הזה הם מספרים מדומים: {% equation %}i{% endequation %} ו-{% equation %}-i{% endequation %}. הם שייכים לשדה {% equation %}\mathbb{C}{% endequation %} אבל לא לשדה {% equation %}\mathbb{R}{% endequation %}. זה אומר שאם יש מטריצה שהפולינום האופייני שלה הוא {% equation %}x^{2}+1{% endequation %}, היא תהיה לכסינה מעל {% equation %}\mathbb{C}{% endequation %} אבל לא מעל {% equation %}\mathbb{R}{% endequation %}. למה? כי ה-{% equation %}P{% endequation %} המלכסנת תהיה חייבת להיות עם מקדמים שהם לא ממשיים (או באופן שקול, הבסיס שבו הטרנספורמציה הרלוונטית תיוצג על ידי מטריצה אלכסונית יהיה עם וקטורים שהכניסות שלהם לא כולן ממשיות).

זה מביא אותנו אל <strong>הצורה הרציונלית</strong> שחומקת גם מהבעיה הזו. כל מטריצה דומה למטריצה בצורה הרציונלית. בלי תלות בשאלות כמו לכסינה/לא לכסינה. בלי תלות בשאלות כמו האם כל השורשים בשדה או לא. תמיד. המחיר שאנחנו משלמים? זו לא צורה עד כדי כך פשוטה; היא בוודאי פחות אינפורמטיבית מאשר צורת ז'ורדן.

בואו נטפל קודם כל בצורה הרציונלית, ואז בצורת ז'ורדן.

<strong>הצורה הרציונלית</strong>

מטריצה בצורה הרציונלית היא גם כן מטריצת בלוקים, כאשר כל בלוק הוא <strong>מטריצה מלווה</strong> של פולינום מסויים. מה זו מטריצה מלווה? בהינתן פולינום מתוקן {% equation %}x^{d}+a_{d-1}x^{d-1}+\dots+a_{1}x+a_{0}{% endequation %}, המטריצה המלווה שלו היא המטריצה

{% equation %}\left(\begin{array}{ccccc}0 &amp; 0 &amp; 0 &amp; \cdots &amp; -a_{0}\\1 &amp; 0 &amp; 0 &amp; \cdots &amp; -a_{1}\\0 &amp; 1 &amp; 0 &amp; \cdots &amp; -a_{2}\\\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots\\0 &amp; 0 &amp; 0 &amp; \cdots &amp; -a_{d-1}\end{array}\right){% endequation %}

כלומר, מטריצה שכולה אפסים למעט האלכסון <strong>מתחת</strong> לאלכסון הראשי שכולו 1-ים, ולמעט הטור האחרון במטריצה שכולל את המקדמים של הפולינום, עם סימן מינוס עליהם. זה... זה לא נראה נחמד במיוחד, אני יודע. בטח נראה פחות נחמד מצורת ז'ורדן. עדיין, אני מקווה שנתיידד קצת עם היצור המוזר הזה בקרוב, אחרי שנבין מאיפה הצורה ה"מוזרה" שלו מגיעה.

מכיוון שכל בלוק שהוא מטריצה מלווה של פולינום נקבע באופן יחיד על פי הפולינום הזה, מה שמאפיין את הצורה הרציונלית הוא סדרת הפולינומים שמכתיבה את סדרת הבלוקים. כלומר, יש לנו סדרת פולינומים {% equation %}p_{1},p_{2},\dots,p_{k}{% endequation %} שמגדירה באופן יחיד את מטריצת הבלוקים הרלוונטית. הדרישה שלנו מהצורה הרציונלית היא שבסדרת הפולינומים הזו, כל פולינום יחלק את קודמו. כלומר, {% equation %}p_{i+1}{% endequation %} מחלק את {% equation %}p_{i}{% endequation %} לכל {% equation %}1\le i&lt;k{% endequation %}.

אחדד את זה על ידי כך שאצטט במפורש את המשפט הרלוונטי: לכל מטריצה ריבועית {% equation %}A{% endequation %}, מעל כל שדה, קיימת מטריצה יחידה {% equation %}B{% endequation %} כך ש-{% equation %}B=P^{-1}AP{% endequation %} עבור {% equation %}P{% endequation %} הפיכה כלשהי, ו-{% equation %}B{% endequation %} היא בצורה רציונלית, דהיינו היא מטריצת בלוקים שבה הבלוקים הם מטריצות מלווות של סדרת פולינומים {% equation %}p_{1},p_{2},\dots,p_{k}{% endequation %} שבה כל פולינום מחלק את קודמו:

{% equation %}B=\left(\begin{array}{cccc}B_{1}\\ &amp; B_{2}\\ &amp; &amp; \ddots\\ &amp; &amp; &amp; B_{k}\end{array}\right){% endequation %}

כך ש-{% equation %}B_{i}{% endequation %} היא המטריצה המלווה של הפולינום {% equation %}p_{i}{% endequation %}.

אני רוצה לחדד עוד קצת את המשמעות של ה<strong>יחידה</strong> הזה: זה אומר שאם קיימת מטריצה {% equation %}C{% endequation %} כך ש-{% equation %}C=Q^{-1}AQ{% endequation %} עבור {% equation %}Q{% endequation %} הפיכה כלשהי, ו-{% equation %}C{% endequation %} היא בצורה רציונלית עם סדרת הפולינומים {% equation %}q_{1},\dots,q_{t}{% endequation %} אז {% equation %}t=k{% endequation %} ו-{% equation %}q_{i}=p_{i}{% endequation %} לכל {% equation %}1\le i\le k{% endequation %}.

יפה. עכשיו כשאנחנו מבינים מה זה אומר, בואו נבין איך מגיעים לזה. ראשית כל נבין מה הקטע הזה עם מטריצות בלוקים. הצורה הרציונלית זו מטריצת בלוקים. גם צורת ז'ורדן זו מטריצת בלוקים. בלוקים בלוקים בלוקים. למה זה? ובכן, זו תוצאה ישירה של כך שאנחנו מחלקים את המרחב הוקטור {% equation %}V{% endequation %} שלנו לתתי-מרחבים <strong>אינווריאנטיים</strong> ביחס לטרנספורמציה {% equation %}T{% endequation %} שאנחנו מוצאים לה את הצורה הקנונית. תת-מרחב {% equation %}W\subseteq V{% endequation %} הוא אינוריאנטי ביחס ל-{% equation %}T{% endequation %} אם {% equation %}T\left(W\right)\subseteq W{% endequation %}. כלומר, אם מפעילים את {% equation %}T{% endequation %} על משהו ב-{% equation %}W{% endequation %} מקבלים משהו ב-{% equation %}W{% endequation %}. עכשיו, אם {% equation %}V=W_{1}\oplus W_{2}\oplus\dots\oplus W_{k}{% endequation %} כאשר כל ה-{% equation %}W{% endequation %}-ים הם אינוריאנטיים ביחס ל-{% equation %}T{% endequation %}, אז אפשר לקחת בסיס לכל אחד מה-{% equation %}W{% endequation %}-ים בנפרד ואז איחוד כל הבסיסים הללו יהיה בסיס ל-{% equation %}V{% endequation %} (כאן חשוב שהסכום יהיה סכום ישר אחרת לאו דווקא נקבל בסיס). בבסיס הזה המטריצה המייצגת של {% equation %}T{% endequation %} תהיה מטריצת בלוקים כאשר כל בלוק מתאים לאחד מתתי-המרחבים {% equation %}W{% endequation %}. למה? כי בואו נזכור מה זו מטריצה מייצגת: אם הבסיס שלנו הוא {% equation %}B=\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} אז העמודה ה-{% equation %}i{% endequation %} בה היא וקטור הקואורדינטות של {% equation %}T\left(b_{i}\right){% endequation %} על פי הבסיס {% equation %}B{% endequation %}. כעת, אצלנו כל איבר בסיס {% equation %}b_{i}{% endequation %} שכזה שייך לאחד מה-{% equation %}W{% endequation %}-ים, ולכן הקואורדינטות היחידות שאולי לא יהיו 0 ב-{% equation %}T\left(b_{i}\right){% endequation %} יהיו שייכות לאברי הבסיס של אותו {% equation %}W{% endequation %}. למשל, אם {% equation %}W{% endequation %} הראשון נפרש על ידי {% equation %}b_{1},b_{2},b_{3},b_{4}{% endequation %}, אז {% equation %}T\left(b_{1}\right){% endequation %} יתן לנו עמודה שהיא כולה אפסים חוץ אולי מ-4 הכניסות הראשונות, וכך גם {% equation %}T\left(b_{2}\right),T\left(b_{3}\right),T\left(b_{4}\right){% endequation %}. קיבלנו שבארבע העמודות הראשונות הכל יהיה אפסים חוץ אולי מהבלוק מגודל 4 שיושב על האלכסון הראשי. וכך זה נמשך.

אם כן, זה הרעיון הן בצורה הרציונלית והן בצורת ז'ורדן - מחלקים איכשהו את {% equation %}V{% endequation %} לתתי-מרחבים אינוריאנטיים, שכאשר <strong>מצמצמים</strong> את {% equation %}T{% endequation %} אליהם, המטריצה המייצגת שלה יוצאת פשוטה יחסית - בלוק ז'ורדן במקרה של צורת ז'ורדן, ומטריצה מלווה במקרה של הצורה הרציונלית. ההבדל בין שתי הצורות הוא באופן שבו מחלקים את המרחב. בסדרת הפוסטים שלי על אלגברה לינארית הראיתי שני משפטים שמפרקים את {% equation %}V{% endequation %} לסכום ישר של תתי-מרחבים אינוריאנטיים "מעניינים": <a href="http://www.gadial.net/2012/01/09/primary_decomposition_theorem/">משפט הפירוק הפרימרי </a>ו<a href="http://www.gadial.net/2016/09/29/cyclic_decomposition_theorem/">משפט הפירוק הציקלי</a>. הצורה הרציונלית היא מה שמתקבל כמעט מייד ממשפט הפירוק הציקלי; כפי שתכף נראה, הצורה הרציונלית היא פשוט דרך אחרת לנסח את משפט הפירוק הציקלי. צורת ז'ורדן מתקבלת מהפירוק הפרימרי, כשאחריו מטפלים בכל תת-מרחב לחוד ומפעילים על אותו תת מרחב את משפט הפירוק הציקלי, אבל עבור טרנספורמציה לינארית אחרת. כלומר, זה שילוב לא לגמרי טריוויאלי של משפטי הפירוק הפרימרי והציקלי, ולכן זה נחמד במיוחד.

נתחיל עם הצורה הרציונלית. מה שצריך לזכור הוא מה הולך במשפט הפירוק הציקלי. אני לא אניח שאתם הולכים לקרוא את הפוסט המפלצתי בנושא, אז בואו נזכיר את זה בקצרה: המשפט אומר שבהינתן {% equation %}V{% endequation %} ובהינתן טרנספורמציה לינארית {% equation %}T{% endequation %} קיים למרחב פירוק {% equation %}V=W_{1}\oplus\dots\oplus W_{k}{% endequation %} שבו כל ה-{% equation %}W{% endequation %}-ים הם מרחבים {% equation %}T{% endequation %}-ציקליים. מה זה מרחב {% equation %}T{% endequation %}-ציקלי? מרחב שמורכב בדיוק מכל הוקטורים שמתקבלים מוקטור מסויים {% equation %}w{% endequation %} ("היוצר") על ידי הפעלות חוזרות ונשנות של {% equation %}T{% endequation %}. כתבתי את זה במקור בתור {% equation %}Z\left(w;T\right)\triangleq\mbox{span}\left\{ T^{0}\left(w\right),T^{1}\left(w\right),T^{2}\left(w\right),\dots\right\} {% endequation %} ומהר מאוד התברר שהמרחב הזה שווה בדיוק לקבוצה {% equation %}\left\{ fw\ |\ f\in\mathbb{F}\left[x\right]\right\} {% endequation %} כאשר {% equation %}fw{% endequation %} זה סימון מקוצר ל{% equation %}f\left(T\right)\left(w\right){% endequation %}, כלומר ללקיחת פולינום כלשהו {% equation %}f{% endequation %}, הצבת {% equation %}T{% endequation %} בתוך הפולינום וקבלת טרנספורמציה לינארית, ואז הפעלה שלה על {% equation %}w{% endequation %}.

מה שנחמד במרחבים הללו הוא שהבסיס שלהם הוא פשוט במיוחד ביחס ל-{% equation %}T{% endequation %}: הוא בסך הכל מהצורה {% equation %}\left\{ T^{0}\left(w\right),T^{1}\left(w\right),\dots,T^{n-1}\left(w\right)\right\} {% endequation %}. מהו {% equation %}n{% endequation %}? ובכן, בואו נזכור שקיימים פולינומים שמתאפסים כאשר מציבים בהם את {% equation %}T{% endequation %}, ולפולינום המתוקן מהמעלה החיובית הקטנה ביותר שמאפס את {% equation %}T{% endequation %} קוראים <strong>הפולינום המינימלי</strong> של {% equation %}T{% endequation %}. אם נסמן אותו ב-{% equation %}m_{T}{% endequation %}, אז אנחנו יודעים ש-{% equation %}m_{T}w=0{% endequation %}. זה מראה שקיים פולינום <strong>כלשהו</strong> שמאפס את {% equation %}w{% endequation %}, אבל ייתכן שיש כאלו שקטנים אפילו יותר מ-{% equation %}m_{T}{% endequation %}. את הפולינום המתוקן המינימלי <strong>מביניהם</strong> אסמן ב-{% equation %}p{% endequation %} ואקרא לו <strong>המאפס</strong> של {% equation %}w{% endequation %}. כעת, {% equation %}n{% endequation %} היא בסך הכל הדרגה של {% equation %}p{% endequation %}. בואו נכתוב את {% equation %}p{% endequation %} באופן מפורש:

{% equation %}p\left(x\right)=x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %}

כאן המקדם של {% equation %}x^{n}{% endequation %} הוא 1 כי אמרנו ש-{% equation %}p{% endequation %} הוא פולינום מתוקן. על שאר המקדמים אני לא מניח כלום. כעת, אם נציב בפולינום הזה את {% equation %}T{% endequation %} ונפעיל את כל זה על {% equation %}w{% endequation %}, נקבל:

{% equation %}\left(T^{n}+a_{n-1}T^{n-1}+\dots+a_{1}T+a_{0}\right)w=0{% endequation %}

ואחרי העברת אגפים נקבל

{% equation %}T^{n}w=-a_{n-1}T^{n-1}w-\dots-a_{1}Tw-a_{0}w{% endequation %}

זה מסביר למה לא "צריך" את הוקטור {% equation %}T^{n}w{% endequation %} או חזקות נוספות של {% equation %}T{% endequation %} בבסיס עבור {% equation %}W{% endequation %}: אנחנו מתחילים לקבל צירופים לינאריים של וקטורים שכבר יש לנו. אבל המשוואה שלמעלה מעניינת לא רק בגלל זה; אתם כבר רואים איך מקבלים מפה את המבנה המוזר של המטריצה המלווה?

בואו נסמן את הבסיס {% equation %}\left\{ T^{0}\left(w\right),T^{1}\left(w\right),\dots,T^{n-1}\left(w\right)\right\} {% endequation %} בתור {% equation %}\mathcal{B}=\left\{ b_{0},b_{1},\dots,b_{n-1}\right\} {% endequation %}. כלומר, {% equation %}b_{i}=T^{i}\left(w\right){% endequation %}. כדי לדעת איך נראית המטריצה המייצגת של {% equation %}T{% endequation %} בבסיס {% equation %}\mathcal{B}{% endequation %} אנחנו צריכים להפעיל את {% equation %}T{% endequation %} על כל איבר בסיס ולראות את וקטור הקואורדינטות המתקבל. עבור רובם זה קל: {% equation %}T\left(b_{0}\right)=T\left(T^{0}\left(w\right)\right)=T^{1}\left(w\right)=b_{1}{% endequation %}, ובאופן דומה {% equation %}T\left(b_{1}\right)=b_{2}{% endequation %} וכן הלאה. זה אומר שוקטור העמודה שמתאים לעמודה של {% equation %}b_{i}{% endequation %} יכיל 1 בודד, בשורה ה-{% equation %}i+1{% endequation %} - כלומר, בדיוק מתחת לאלכסון הראשי. כל זה נכון עד לעמודה האחרונה, כלומר עד ל-{% equation %}T\left(b_{n}\right){% endequation %}. כאן אנחנו משתמשים במשוואה שכתבתי למעלה ומקבלים

{% equation %}T\left(b_{n}\right)=-a_{n-1}b_{n-1}-\dots-a_{1}b_{1}-a_{0}b_{0}{% endequation %}

וזה נותן לנו בדיוק את העמודה הימנית ביותר של המטריצה המלווה של {% equation %}p{% endequation %}. קיבלנו, אם כן, שהמטריצה המייצגת של {% equation %}T{% endequation %} (כאשר {% equation %}T{% endequation %} מצומצמת ל-{% equation %}W{% endequation %}) בבסיס {% equation %}\mathcal{B}{% endequation %} היא בדיוק המטריצה המלווה של {% equation %}p{% endequation %}, כאשר {% equation %}p{% endequation %} הוא המאפס של {% equation %}w{% endequation %}, שהוא היוצר של {% equation %}W{% endequation %}.

החתיכה האחרונה בפאזל הזה הוא הדבר הנוסף שמשפט הפירוק הציקלי נותן לנו: הוא אומר שאם {% equation %}V=W_{1}\oplus\dots\oplus W_{k}{% endequation %} כאשר {% equation %}W_{i}=Z\left(w_{i};T\right){% endequation %} , ואם נסמן את המאפס של {% equation %}w_{i}{% endequation %} ב-{% equation %}p_{i}{% endequation %}, אז המאפסים הללו מקיימים את יחס החלוקה שבו כל מאפס מחלק את קודמו: {% equation %}p_{i+1}{% endequation %} מחלק את {% equation %}p_{i}{% endequation %}, והוא אומר שסדרת הפולינומים הללו היא <strong>יחידה</strong>. שימו לב: הוא לא אומר "יש פירוק יחיד לתת-מרחבים ציקליים" כי זה לא נכון; כל מה שהוא אומר הוא שסדרת המאפסים שלהם, עם תנאי החלוקה הזה, היא יחידה. זה בדיוק מה שהיה חסר לנו. סדרת הפולינומים {% equation %}p_{1},\dots,p_{k}{% endequation %} הזו מגדירה לנו את הצורה הרציונלית בצורה מלאה. הצורה הרציונלית הרי לא תלויה ב-{% equation %}w{% endequation %}-ים או אפילו ב-{% equation %}W{% endequation %}-ים; מה שקובע את המטריצה בסופו של דבר הוא רק סדרת הפולינומים (וכן, יכולים להיות בסיסים שונים שבכולם {% equation %}T{% endequation %} מיוצגת על ידי אותה מטריצה שהיא בצורה רציונלית, אין עם זה בעיה).

הפולינומים {% equation %}p_{1},\dots,p_{k}{% endequation %} הללו נקראים <strong>הגורמים האינוריאנטיים</strong> של {% equation %}T{% endequation %}. כעת, משראינו שהם תמיד קיימים, נשאלת השאלה הפשוטה - בהינתן מטריצה {% equation %}A{% endequation %}, איך מוצאים את הגורמים האינוריאנטיים שלה? למשפט הפירוק הציקלי אין הוכחה קונסטרוקטיבית במיוחד - שלב מרכזי שם הוא "ניקח וקטור שממקסם כך וכך ונעשה איתו ניסים ונפלאות" בלי ממש להסביר איך מוצאים את הוקטור הזה. האם יש אלגוריתם פשוט יחסית למציאת הגורמים האינוריאנטיים? באופן מפתיע (עבורי) יש כזה, והוא מאוד דומה לדירוג מטריצות. רק שבמקום לדרג את {% equation %}A{% endequation %} מדרגים את המטריצה {% equation %}xI-A{% endequation %} (שהיא מטריצה שחיה מעל החוג {% equation %}\mathbb{F}\left[x\right]{% endequation %} ולא מעל השדה {% equation %}\mathbb{F}{% endequation %}), ופעולות הדירוג שלנו הן:
<ol>
	<li>החלפת שתי שורות או עמודות.</li>
	<li>הוספה לשורה אחת של שורה אחת שמוכפלת בסקלר מתוך {% equation %}\mathbb{F}\left[x\right]{% endequation %} (דהיינו, מוכפלת בפולינום כלשהו מעל {% equation %}\mathbb{F}{% endequation %}), ואותו הדבר עם עמודות.</li>
	<li>הכפלה של שורה או עמודה אחת ב<strong>איבר הפיך</strong> מתוך {% equation %}\mathbb{F}\left[x\right]{% endequation %}, כלומר באיבר של {% equation %}\mathbb{F}{% endequation %}.</li>
</ol>
אלמלא התנאי המעט שונה ב-3 והעובדה שאפשר לפעול גם על עמודות, זה היה בדיוק דירוג מטריצות כמו שרואים כשרק מתחילים להתעסק עם אלגברה לינארית. אבל מה היעד שלו? בדירוג מטריצות "רגיל" היעד הוא להגיע למטריצה שבה כל הכניסות הן 0 למעט כניסות שהן 1 ש"אי אפשר לוותר עליהן", ובמקרה שבו {% equation %}A{% endequation %} הפיכה נקבל שיש 1-ים בדיוק על האלכסון הראשי. במקרה שלנו מובטח שנוכל לאפס את כל מה שאינו על האלכסון הראשי, אבל על האלכסון הראשי עשויים להישאר פולינומים, ועל ידי החלפות מתאימות אפשר להביא את המטריצה לצורה הבאה:

{% equation %}\left(\begin{array}{ccccccc}1\\ &amp; \ddots\\ &amp; &amp; 1\\ &amp; &amp; &amp; a_{1}\left(x\right)\\ &amp; &amp; &amp; &amp; a_{2}\left(x\right)\\ &amp; &amp; &amp; &amp; &amp; \ddots\\ &amp; &amp; &amp; &amp; &amp; &amp; a_{k}\left(x\right)\end{array}\right){% endequation %}

כאשר הפולינומים {% equation %}a\left(x\right){% endequation %} על האלכסון מקיימים את יחסי החלוקה שלנו (כל אחד מחלק את קודמו). הצורה הזו נקראת <strong>הצורה הנורמלית של סמית</strong> (לפעמים מגדירים הפוך, שכל פולינום מחלק את הבא אחריו, אבל מה זה משנה). להוכיח שכל זה באמת עובד? זה עניין לפוסט נפרד.

והנה הערה מעניינת לסיום, שתהיה מעניינת עוד יותר עוד רגע, כשנגיע לצורת ז'ורדן: הגורמים האינוריאנטים הם לא סתם פולינומים אקראיים. הם קשורים בקשר הדוק מאוד לפולינומים המינימלי והאופייני של {% equation %}T{% endequation %}. ליתר דיוק: {% equation %}p_{1}{% endequation %} (הגורם האינוריאנטי הראשון, הגדול ביותר, זה שמתחלק על ידי היתר) הוא בדיוק הפולינום המינימלי, ואילו המכפלה {% equation %}p_{1}\cdots p_{k}{% endequation %} היא בדיוק הפולינום האופייני של {% equation %}T{% endequation %}. למה? ובכן, זה לא טריוויאלי. את זה ש-{% equation %}p_{1}{% endequation %} הוא הפולינום המינימלי של {% equation %}T{% endequation %} הראיתי במובלע בהוכחת שלב ה"יחידות" של משפט הפירוק הציקלי; הרעיון הוא שאם {% equation %}V{% endequation %} הוא סכום ישר של מרחבים ציקליים, והמאפסים של <strong>כל</strong> המרחבים הציקליים הללו מחלקים את {% equation %}p_{1}{% endequation %}, אז הפעלת {% equation %}p_{1}{% endequation %} על איבר כלשהו של המרחב מאפסת את כל הרכיבים שלו ולכן מאפסת אותו. לכן הפולינום המינימלי מחלק את המאפס {% equation %}p_{1}{% endequation %}. מצד שני, המאפסים תמיד מחלקים את הפולינום המינימלי.

דרך פשוטה לראות שמכפלת כל הגורמים האינוריאנטיים היא הפולינום האופייני היא לזכור שהפולינום האופייני הוא הדטרמיננטה, מעל {% equation %}\mathbb{F}\left[x\right]{% endequation %}, של המטריצה {% equation %}xI-A{% endequation %}, ולזכור שדטרמיננטה <strong>לא משתנה</strong> על ידי פעולות אלמנטריות, פרט לכך שכפל בסקלר כלשהו של שורה כופל גם את הדטרמיננטה בסקלר הזה (זאת להבדיל מהוספה של כפולה בסקלר של שורה לשורה אחרת, ש<strong>אינה</strong> משנה את הדטרמיננטה). אצלנו, התנאי לכפל בסקלר הוא שהסקלר יהיה שייך ל-{% equation %}\mathbb{F}{% endequation %}, כלומר הפיך; כלומר, הפולינום שהוא הדטרמיננטה שנקבל בסופו של דבר יהיה זהה לפולינום האופייני עד כדי כפל באיבר של {% equation %}\mathbb{F}{% endequation %}; אבל הפולינום האופייני הוא מתוקן, וגם הדטרמיננטה של צורת סמית היא פולינום מתוקן (מכפלה של פולינומים מתוקנים) כך שהם יהיו שווים.

עכשיו אפשר לעבור אל צורת ז'ורדן סוף סוף.

<strong>צורת ז'ורדן</strong>

הנה דרך ציורית לחשוב על ההבדל בין הצורה הרציונלית וצורת ז'ורדן של {% equation %}T{% endequation %}: בצורה הרציונלית, אנחנו לוקחים את הפולינום המינימלי של {% equation %}T{% endequation %} ומתחילים לקחת סדרת מחלקים שלו - <strong>הגורמים האינוריאנטיים</strong> שלו. בצורת ז'ורדן, אנחנו לוקחים את אותו פולינום מינימלי ו<strong>מפרקים אותו לגורמים אי פריקים</strong> - זה נקרא "<strong>המחלקים האלמנטריים</strong>" שלו. חלוקה כזו לגורמים אי-פריקים היא מה שמשפט הפירוק הפרימרי עושה; הרעיון בצורת ז'ורדן הוא לקחת את התוצאה של משפט הפירוק הפרימרי ולהראות שבמקרה שבו הפולינום התפרק לגורמים לינאריים, אפשר לתת ניתוח יפה של כל גורם כזה בנפרד.

בואו ניזכר מה אומר משפט הפירוק הפרימרי. ניקח את הפולינום המינימלי {% equation %}m_{T}{% endequation %} של {% equation %}T{% endequation %}, ונפרק אותו לגורמים אי-פריקים (כלומר, למכפלה של פולינומים שהם בעצמם לא מכפלות של פולינומים ששניהם ממעלה גדולה מ-0). נסמן את זה {% equation %}m_{T}=p_{1}^{r_{1}}\cdots p_{k}^{r_{k}}{% endequation %}. אז אפשר לפרק את {% equation %}V{% endequation %} לסכום ישר של תתי-מרחבים {% equation %}T{% endequation %}-אינוריאנטיים {% equation %}V=W_{1}\oplus\dots\oplus W_{k}{% endequation %} שמוגדרים כך: {% equation %}W_{i}=\ker\left(p_{i}^{r_{i}}\left(T\right)\right){% endequation %}.

הדיון הזה הוא קצת באוויר מבחינתנו אז בואו נרד לקרקע ונדבר על מה קורה במקרה שמתאים לצורת ז'ורדן, כלומר שבו {% equation %}m_{T}{% endequation %} מתפרק לגורמים לינאריים: במקרה הזה אפשר לכתוב {% equation %}m_{T}=\left(x-\lambda_{1}\right)^{r_{1}}\cdots\left(x-\lambda_{k}\right)^{r_{k}}{% endequation %} כאשר {% equation %}\lambda_{1},\dots,\lambda_{k}{% endequation %} הם השורשים של הפולינום המינימלי. במקרה הזה, המרחב {% equation %}W_{i}{% endequation %} הוא בדיוק {% equation %}\ker\left(\left(T-\lambda_{i}I\right)^{r_{i}}\right){% endequation %}. מה שנותר לנו להבין, אם כן, הוא איך נראית המטריצה המייצגת של {% equation %}T{% endequation %} כשהיא מצומצמת לתת-מרחב מהצורה {% equation %}W=\ker\left(\left(T-\lambda I\right)^{r}\right){% endequation %}. מה שנראה הוא שהמטריצה הזו תהיה מטריצת בלוקים, שכולם בלוקי ז'ורדן שמתאימים לערך העצמי {% equation %}\lambda{% endequation %}. כלומר, יש לנו עכשיו הרבה פחות עבודה - במקום להבין את {% equation %}T{% endequation %} באופן כללי, מספיק להבין אותה על תת-מרחב שבו היא תהיה פשוטה יחסית. מכאן ואילך אני אמשיך לדבר על {% equation %}T{% endequation %}, אבל מה שאני אתכוון אליו בתכל'ס יהיה {% equation %}T|_{W}{% endequation %}, כלומר {% equation %}T{% endequation %} שמצומצמת לתת-המרחב {% equation %}W{% endequation %}.

הפאנץ' המרכזי כאן הוא שעל תת-המרחב {% equation %}W{% endequation %}, {% equation %}T{% endequation %} היא סכום של שתי טרנספורמציות לינאריות פשוטות במיוחד: אחת שהיא <strong>סקלרית</strong> ואחת שהיא <strong>נילפוטנטית</strong>. אני יכול לכתוב {% equation %}T=D+N{% endequation %} כאשר {% equation %}D{% endequation %} היא הטרנספורמציה {% equation %}D=\lambda I{% endequation %} שפשוט כופלת הכל ב-{% equation %}\lambda{% endequation %} ({% equation %}D\left(v\right)=\lambda v{% endequation %}) והמטריצה המייצגת שלה <strong>בכל בסיס</strong> היא בסך הכל המטריצה הסקלרית שכולה אפסים למעט האלכסון הראשי שכולו {% equation %}\lambda{% endequation %}. נשאר להבין את {% equation %}N{% endequation %} ולמצוא בסיס שבו המטריצה המייצגת שלה תהיה נחמדה.

אני, כאמור, טוען ש-{% equation %}N{% endequation %} היא נילפוטנטית. מה זו טרנספורמציה נילפוטנטית? כזו שאם מעלים אותה בחזקה מספיק פעמים, מקבלים את טרנספורמציית האפס. הנה דוגמה למטריצה נילפוטנטית:

{% equation %}\left(\begin{array}{ccccc}0 &amp; 1 &amp; 0 &amp; 0 &amp; 0\\0 &amp; 0 &amp; 1 &amp; 0 &amp; 0\\0 &amp; 0 &amp; 0 &amp; 0 &amp; 0\\0 &amp; 0 &amp; 0 &amp; 0 &amp; 1\\0 &amp; 0 &amp; 0 &amp; 0 &amp; 0\end{array}\right){% endequation %}

תעלו אותה בחזקה מספיק פעמים ותקבלו את מטריצת האפס. כעת, לא בחרתי את המטריצה הזו באקראי - בחרתי מטריצה שבה יש 1-ים רק במקום אחד: על האלכסון שמעל האלכסון הראשי. בדיוק כמו שקורה בצורת ז'ורדן. למעשה, המטריצה הזו היא-היא צורת ז'ורדן של טרנספורמציה כלשהי שכל הערכים העצמיים שלה הם 0.

מכיוון שהגדרתי {% equation %}D=\lambda I{% endequation %} הרי שאם אני מגדיר {% equation %}N=T-\lambda I{% endequation %} אני מקבל בדיוק ש-{% equation %}T=D+N{% endequation %} כפי שכתבתי למעלה. את {% equation %}T-\lambda I{% endequation %} אנחנו מכירים: המרחב {% equation %}W{% endequation %} <strong>הוגדר</strong> בתור הגרעין של {% equation %}\left(T-\lambda I\right)^{r}{% endequation %}, דהיינו כל אברי {% equation %}W{% endequation %} שייכים לגרעין של {% equation %}N^{r}{% endequation %}, דהיינו {% equation %}N^{r}{% endequation %} היא טרנספורמציית האפס על <strong>כל</strong> המרחב {% equation %}W{% endequation %}, ולכן {% equation %}N{% endequation %} נילפונטנטית כפי שהבטחתי.

אבל למה זה מעניין?

זה מעניין כי עכשיו אני הולך להשתמש <strong>במשפט הפירוק הציקלי</strong> על המרחב {% equation %}W{% endequation %} והטרנספורמציה {% equation %}N{% endequation %}. במילים אחרות, אני הולך למצוא את <strong>הצורה הרציונלית</strong> של {% equation %}N{% endequation %} על {% equation %}W{% endequation %}, ומכיוון ש-{% equation %}N{% endequation %} נילפוטנטית הצורה הרציונלית הזו תהיה פשוטה במיוחד. המשמעות של נילפוטנטיות היא שהפולינום המינימלי של {% equation %}N{% endequation %} הוא פשוט במיוחד: הוא חייב לחלק את {% equation %}x^{r}{% endequation %} (כי {% equation %}N{% endequation %} מאפסת את הפולינום {% equation %}x^{r}{% endequation %}) ולכן הוא בעצמו מהצורה {% equation %}x^{t}{% endequation %} עבור {% equation %}t{% endequation %} כלשהו. מכיוון שכל הגורמים האינוריאנטיים של {% equation %}N{% endequation %} מחלקים את הפולינום המינימלי, נובע שכל הגורמים האינוריאנטיים של {% equation %}N{% endequation %} הם מהצורה {% equation %}x^{t}{% endequation %} עבור {% equation %}t{% endequation %} כלשהו.

ולמה זה כל כך טוב? כי תחשבו שניה מהי המטריצה המלווה של הפולינום {% equation %}x^{t}{% endequation %}: כל העמודה האחרונה, שבדרך כלל מלאה מקדמים מכוערים עם מינוסים מכוערים, תהיה פשוט אפסים! זאת מכיוון שכל המקדמים של {% equation %}x^{t}{% endequation %} למעט המקדם המוביל (שלא מופיע במטריצה המלווה) הם אפס. זה אומר שהמטריצה המלווה תהיה מהצורה הבאה:

{% equation %}\left(\begin{array}{ccccc}0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0\\1 &amp; 0 &amp; 0 &amp; \cdots &amp; 0\\0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0\\\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots\\0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0\end{array}\right){% endequation %}

זה כמעט בלוק ז'ורדן - רק עם 1-ים מתחת לאלכסון במקום מעל לאלכסון. זה לא קורה בגלל שהבסיס שאנחנו עובדים איתו שונה, אלא רק שה<strong>סדר</strong> של האיברים בבסיס צריך להיות הפוך. אם אנחנו מגדירים בסיס {% equation %}\mathcal{B}=\left\{ b_{0},b_{1},\dots,b_{n-1}\right\} {% endequation %} על ידי {% equation %}b_{i}=N^{i}u{% endequation %} עבור {% equation %}u{% endequation %} שהוא הוקטור הציקלי שלנו, אז המטריצה המייצגת של {% equation %}N{% endequation %} בבסיס הזה תהיה מה שלמעלה. אבל אם נהפוך את הסדר של האיברים בבסיס, כלומר נגדיר {% equation %}b_{i}=N^{\left(n-1\right)-i}u{% endequation %}, אז יתקיים {% equation %}N\left(b_{i}\right)=b_{i-1}{% endequation %} לכל {% equation %}1\le i&lt;n{% endequation %}, ואילו עבור {% equation %}b_{0}{% endequation %} יתקיים {% equation %}N\left(b_{0}\right)=N\left(N^{n-1}\right)u=N^{n}u=0{% endequation %}. לכן המטריצה המייצגת בבסיס ההפוך הזה תהיה

{% equation %}\left(\begin{array}{ccccc}0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0\\0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0\\0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0\\\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots\\0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1\\0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0\end{array}\right){% endequation %}

וזה בדיוק בלוק ז'ורדן.

נסכם: התחלנו עם {% equation %}T{% endequation %}. אמרנו שנמצא מטריצה מייצגת עבור {% equation %}T{% endequation %} שבה לכל ערך עצמי {% equation %}\lambda{% endequation %} של {% equation %}T{% endequation %} יהיה לנו בלוק אחד במטריצה שהוא המטריצה המייצגת של {% equation %}T{% endequation %} המצומצמת למרחב {% equation %}W=\ker\left(\left(T-\lambda I\right)^{r}\right){% endequation %} - זה משפט הפירוק הפרימרי. ב-{% equation %}W{% endequation %} אמרנו שנפרק את {% equation %}T{% endequation %} לסכום {% equation %}T=D+N{% endequation %} כאשר {% equation %}D{% endequation %} סקלרית ואילו {% equation %}N{% endequation %} נילפוטנטית, ואז השתמשנו במשפט הפירוק הציקלי כדי להראות שהמטריצה המייצגת של {% equation %}N{% endequation %} היא מטריצת בלוקים שבה כל בלוק הוא בלוק ז'ורדן שמתאים לערך העצמי 0, כלומר עם 0 על האלכסון הראשי. המטריצה המייצגת של {% equation %}T{% endequation %} על {% equation %}W{% endequation %}, אם כן, היא סכום של שתי מטריצות שאחת מהן היא {% equation %}\left(\begin{array}{cccc}\lambda\\ &amp; \lambda\\ &amp; &amp; \ddots\\ &amp; &amp; &amp; \lambda\end{array}\right){% endequation %} והשניה היא 0 בכל מקום חוץ אולי מכמה 1-ים באלכסון שמעל האלכסון הראשי.

הראינו קיום, אבל מה עם יחידות? ובכן, הפירוק הפרימרי הוא בוודאי יחיד, כי קיים רק פירוק אחד לגורמים אי פריקים של הפולינום המינימלי (זה מתקשר לדוגמה שנתתי בתחילת הפוסט, של פירוק יחיד לאי פריקים במספרים הטבעיים; עם פולינומים זה אותו סיפור בדיוק). לכל בלוק שנותן הפירוק הפרימרי היחידות שלו נובעת מהיחידות של הצורה הרציונלית. זה מסיים גם את זה.

נשאלת כמובן גם השאלה איך מוצאים את צורת ז'ורדן בפועל. אנחנו רואים שיש פה שני שלבים: ראשית צריך לפרק את הפולינום המינימלי לגורמים בשביל לקבל את הפירוק הפרימרי. שנית, צריך למצוא את בלוקי ז'ורדן שמתאימים לכל ערך עצמי, וזה בעצם שקול למציאת הצורה הרציונלית של {% equation %}N{% endequation %} עבור כל מרחב של הפירוק הפרימרי. אפשר לעשות את זה עם צורת סמית כמו שתיארתי כאן, אבל כבר קל יותר פשוט למצוא את הוקטורים הציקליים באופן מפורש. זה בדיוק מה שתיארתי <a href="http://www.gadial.net/2016/08/30/jordan_form_basics/">בפוסט על התכל'ס של מציאת צורת ז'ורדן</a>.

עכשיו אפשר גם לדבר על שלוש תכונות של הבלוקים בצורת ז'ורדן שהזכרתי בפוסט ההוא, ולראות למה הן נכונות. אזכיר אותן:
<ul>
	<li>לכל ערך עצמי {% equation %}\lambda{% endequation %}, הריבוי האלגברי של {% equation %}\lambda{% endequation %} (הדרגה של {% equation %}\left(x-\lambda\right){% endequation %} בפולינום האופייני) שווה ל<strong>סכום גדלי</strong> בלוקי ז'ורדן המתאימים ל-{% equation %}\lambda{% endequation %}.</li>
	<li>לכל ערך עצמי {% equation %}\lambda{% endequation %}, הריבוי הגאומטרי של {% equation %}\lambda{% endequation %} שווה ל<strong>מספר</strong> בלוקי ז'ורדן המתאימים ל-{% equation %}\lambda{% endequation %}.</li>
	<li>לכל ערך עצמי {% equation %}\lambda{% endequation %}, הריבוי של {% equation %}\lambda{% endequation %} <strong>בפולינום המינימלי</strong> שווה לגודל בלוק הז'ורדן הגדול ביותר המתאים ל-{% equation %}\lambda{% endequation %}.</li>
</ul>
התכונה הראשונה קלה למדי: אם {% equation %}J{% endequation %} היא מטריצה בצורת ז'ורדן, טריוויאלי לחשב את הפולינום האופייני שלה - מכיוון ש-{% equation %}xI-J{% endequation %} היא מטריצה משולשית עליונה, הדטרמיננטה שלה היא מכפלת אברי האלכסון. לכן הריבוי האלגברי של {% equation %}\lambda{% endequation %} זהה למספר הפעמים ש-{% equation %}\lambda{% endequation %} מופיע על האלכסון של {% equation %}J{% endequation %}, שהוא סכום הגדלים של הבלוקים שבהם {% equation %}\lambda{% endequation %} מופיע. את זה יכולנו לדעת גם בלי להבין מאיפה צורת ז'ורדן מגיעה בכלל.

התכונה השלישית נובעת ממה שאמרנו על הגורמים האינוריאנטיים בצורה הרציונלית: הגורם האינוריאנטי הגדול ביותר שווה לפולינום המינימלי. התכונה השניה טיפה יותר מסובכת: הריבוי הגאומטרי של {% equation %}\lambda{% endequation %} הוא בדיוק {% equation %}\dim\ker N{% endequation %}. לכן השאלה היא מה הגרעין של {% equation %}N{% endequation %} ב-{% equation %}W{% endequation %}. בואו ניזכר מה הוא הבסיס של {% equation %}W{% endequation %} שאנחנו מוצאים בסוף - הוא איחוד של בסיסים לתתי-המרחבים הציקליים שפירקנו את {% equation %}W{% endequation %} אליהם, ובכל תת-מרחב כזה אברי הבסיס הם הפעלות של {% equation %}N{% endequation %} על וקטור ציקלי כלשהו. האיבר האחרון בכל אחד מהבסיסים הללו הוא וקטור שכאשר נפעיל עליו את {% equation %}N{% endequation %} נקבל 0, ולכן הוא שייך ל-{% equation %}\ker N{% endequation %}; שאר הוקטורים בבסיס הם בדיוק כאלו שהפעלה של {% equation %}N{% endequation %} עליהם לא מחזירה 0 (אלא את האיבר הבא בבסיס) ולכן הם לא שייכים ל-{% equation %}\ker N{% endequation %}. כך אנחנו מקבלים שכל וקטור ציקלי תורם בדיוק וקטור בלתי תלוי אחד ל-{% equation %}\ker N{% endequation %}, ולכן המימד של {% equation %}\ker N{% endequation %} שווה למספר בלוקי הז'ורדן (כי כל בלוק ז'ורדן נובע מוקטור ציקלי אחד).

<strong>דברי סיכום ופרידה</strong>

היה הרבה מלל בפוסט הזה, אבל מבחינה מתמטית לא היה כאן שום דבר מסובך, רק הסברים טריוויאליים למדי. הסיבה לכך היא שאת כל העבודה כבר עשינו קודם, עם משפט הפירוק הפרימרי ומשפט הפירוק הציקלי, שההוכחות של שניהם היו טכניות יחסית וכללו רעיונות לא טריוויאליים. אחרי שהשגנו את המשפטים הללו, הכל היה פשוט: הצורה הרציונלית נבעה מיידית ממשפט הפירוק הציקלי, וצורת ז'ורדן נבעה ממשפט הפירוק הפרימרי שאחרי השתמשנו בצורה קצת חכמה במשפט הפירוק הציקלי כדי "לפרק עוד קצת" את מה שקיבלנו ממשפט הפירוק הפרימרי.

אני חושב שהיישומים הללו של המשפטים הם אלגנטיים מאוד. אחרי שמבינים "מאיפה זה מגיע", הן הצורה הרציונלית והן צורת ז'ורדן נראות לי - עד כמה שאפשר לומר את זה על מושג מתמטי, כמובן - יפות. זה מאפיין כללי של אלגברה לינארית, לדעתי; זה תחום שיש בו כמה משפטים ספציפיים שהם טכניים מאוד בהוכחתם, אבל מסביב להם רוב התורה שנבנית היא מאוד פשוטה ואינטואיטיבית והכל בה "פשוט מסתדר מעצמו". אני מקווה שהצלחתי להעביר את התחושה הזו בפוסט הזה.

ועוד דבר אחד לפרידה: הפוסט הזה פחות או יותר סוגר את אחד מהכיוונים בסדרת הפוסטים שלי על אלגברה לינארית (זה שעוסק בצורות קנוניות; מן הסתם יש כיוונים נוספים), אבל אני לא רוצה לתת אשליה שזה סוף הסיפור. כפי שרמזתי בפוסטים קודמים בנושא, את כל מה שעשינו כאן אפשר לראות בתור מקרה פרטי של משפט כללי יותר שעוסק ב<strong>מודולים</strong>, שהם בתורם הכללה של מרחבים וקטוריים. אני מקווה להציג בפוסט יום אחד גם את נקודת המבט הזו, אבל לבינתיים בואו נסתפק בלדעת שהיא קיימת.