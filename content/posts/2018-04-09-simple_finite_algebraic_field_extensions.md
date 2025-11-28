---
id: 3596
title: "הרחבות אלגבריות, פשוטות, סופיות ומי יודע מה עוד"
date: 2018-04-09 22:22:05
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - הרחבת שדות
---
<h2>תזכורת</h2>
<a href="https://gadial.net/2018/04/03/field_extensions_intro/">בפוסט הקודם</a> שלי דיברתי על <strong>הרחבת שדות</strong>. בואו נחזור על עיקרי הדברים כדי שהפוסט הזה יעמוד עד כמה שניתן בזכות עצמו, ונוסיף עוד כמה הגדרות:

אם {% equation %}F,E{% endequation %} הם שני שדות כך ש-{% equation %}F\subseteq E{% endequation %} אז אומרים ש-{% equation %}E{% endequation %} <strong>מרחיב</strong> את {% equation %}F{% endequation %} ומסמנים את זה ב-{% equation %}E/F{% endequation %}. קל לראות ש-{% equation %}E{% endequation %} הוא <strong>מרחב וקטורי</strong> מעל {% equation %}F{% endequation %} והמימד של המרחב הזה מסומן ב-{% equation %}\left[E:F\right]{% endequation %}.

אני מחלק את האיברים ב-{% equation %}E{% endequation %} לשני סוגים: איבר {% equation %}\theta\in E{% endequation %} הוא <strong>אלגברי</strong> מעל {% equation %}F{% endequation %} אם קיים פולינום {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} כך ש-{% equation %}p\left(\theta\right)=0{% endequation %}. אם {% equation %}\theta\in E{% endequation %} הוא לא אלגברי, אני אומר שהוא <strong>טרנסנדנטי</strong>.

אם {% equation %}\theta\in E{% endequation %} הוא איבר כלשהו (אלגברי <strong>או</strong> טרנסנדנטי), אני מסמן ב-{% equation %}F\left(\theta\right){% endequation %} את השדה הקטן ביותר שמכיל את {% equation %}F{% endequation %} ואת {% equation %}\theta{% endequation %}. הדרך המקובלת להוכיח שקיים שדה כזה היא לקחת את חיתוך כל תתי-השדות של {% equation %}E{% endequation %} שמכילים את {% equation %}F,\theta{% endequation %} (למשל, {% equation %}E{% endequation %}); לא קשה להוכיח שחיתוך כלשהו של שדות הוא שדה ושהתוצאה היא השדה הקטן ביותר המבוקש.

עכשיו, הנה כמה מההגדרות המרכזיות על הרחבת שדות {% equation %}E/F{% endequation %} כלשהי:
<ul>
 	<li>אני אומר ש-{% equation %}E/F{% endequation %} <strong>סופית</strong> אם {% equation %}\left[E:F\right]{% endequation %} סופי.</li>
 	<li>אני אומר ש-{% equation %}E/F{% endequation %} <strong>אלגברית</strong> אם <strong>כל</strong> איבר של {% equation %}E{% endequation %} הוא אלגברי מעל {% equation %}F{% endequation %}.</li>
 	<li>אני אומר ש-{% equation %}E/F{% endequation %} <strong>פשוטה</strong> אם {% equation %}E=F\left(\theta\right){% endequation %} עבור {% equation %}\theta\in E{% endequation %} כלשהו; במקרה הזה אני גם אומר ש-{% equation %}\theta{% endequation %} הוא <strong>איבר פרימיטיבי</strong> עבור ההרחבה {% equation %}E/F{% endequation %}.</li>
</ul>
בואו נתחיל מלנסות להבין את הקשרים שיש בין שלוש התכונות הללו.
<h2>הרחבות סופיות, אלגבריות ופשוטות - מי נגד מי?</h2>
בפוסט הקודם ראינו שני עניינים שהם צדדים שונים של אותו המטבע:
<ul>
 	<li>אם {% equation %}F{% endequation %} שדה ו-{% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} פולינום <strong>אי-פריק</strong> אז קיימת הרחבה {% equation %}E/F{% endequation %} ואיבר {% equation %}\theta\in E{% endequation %} כך ש-{% equation %}p\left(\theta\right)=0{% endequation %} ו-{% equation %}F\left(\theta\right)\cong F\left[x\right]/\left\langle p\left(x\right)\right\rangle {% endequation %}.</li>
 	<li>אם {% equation %}E/F{% endequation %} הרחבת שדות ו-{% equation %}\theta\in E{% endequation %} אלגברי מעל {% equation %}F{% endequation %} אז קיים פולינום מתוקן <strong>יחיד </strong>מדרגה חיובית מינימלית, {% equation %}m_{\theta,F}\left(x\right){% endequation %}, כך ש-{% equation %}m_{\theta,F}\left(\theta\right)=0{% endequation %}. הפולינום הזה נקרא <strong>הפולינום המינימלי </strong>של {% equation %}\theta{% endequation %} מעל {% equation %}F{% endequation %}, ומתקיים {% equation %}F\left(\theta\right)\cong F\left[x\right]/\left\langle m_{F}\left(x\right)\right\rangle {% endequation %}.</li>
</ul>
ראינו גם שבמקרה שבו {% equation %}\theta{% endequation %} אלגברי מעל {% equation %}F{% endequation %}, אפשר לתאר את {% equation %}F\left(\theta\right){% endequation %} בתור {% equation %}F\left(\theta\right)=\left\{ p\left(\theta\right)\ |\ p\left(x\right)\in F\left[x\right]\right\} {% endequation %}, כלומר בתור כל הפולינומים ב-{% equation %}\theta{% endequation %} עם מקדמים ב-{% equation %}F{% endequation %}. אם נסמן {% equation %}n=\deg m_{\theta,F}\left(x\right){% endequation %} אז ניתן להסתפק רק בפולינומים ממעלה {% equation %}n-1{% endequation %} לכל היותר; במילים אחרות, {% equation %}F\left(\theta\right){% endequation %} נפרש כמרחב וקטורי מעל {% equation %}F{% endequation %} על ידי הקבוצה {% equation %}\left\{ 1,\theta,\dots,\theta^{n-1}\right\} {% endequation %}.

כדי להשתכנע שזה עובד צריך להשתכנע בשני דברים: שאפשר לכתוב את {% equation %}\theta^{n}{% endequation %} בתור צירוף לינארי של הוקטורים הללו (כך שאפשר להקטין את המעריך של כל חזקה חיובית של {% equation %}\theta{% endequation %} עד שנקבל צירוף לינארי של חזקות מ-0 ועד {% equation %}n-1{% endequation %}), ושאפשר לכתוב את {% equation %}\theta^{-1}{% endequation %} בתור צירוף לינארי שכזה. אם נכתוב במפורש

{% equation %}m_{\theta,F}\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %}

אז נקבל את המשוואה

{% equation %}a_{n}\theta^{n}+\dots+a_{1}\theta+a_{0}=0{% endequation %}

שממנה ניתן לחלץ:

{% equation %}\theta^{n}=-\frac{1}{a_{n}}\left(a_{n-1}\theta^{n-1}+\dots+a_{1}\theta+a_{0}\right){% endequation %}

{% equation %}\theta^{-1}=-\frac{1}{a_{0}}\left(a_{n}\theta^{n-1}+\dots+a_{2}\theta+a_{1}\right){% endequation %}

אם {% equation %}\theta{% endequation %} טרנסנדנטי מעל {% equation %}F{% endequation %} אז התיאור הכי טוב שלנו ל-{% equation %}F\left(\theta\right){% endequation %} הוא בתור המרחב הוקטורי שנפרש על ידי {% equation %}\left\{ \dots,\theta^{-2},\theta^{-1},1,\theta,\theta^{2},\dots\right\} {% endequation %} מעל {% equation %}F{% endequation %}.

מסקנה אחת מהדיון הזה היא זו: אם {% equation %}\theta{% endequation %} אלגברי מעל {% equation %}F{% endequation %} עם פולינום מינימלי ממעלה {% equation %}n{% endequation %}, אז {% equation %}\left[F\left(\theta\right):F\right]=n{% endequation %}. גם הכיוון השני נכון כמעט באותה צורה: נניח ש-{% equation %}\left[F\left(\theta\right):F\right]=n{% endequation %}, אז זה אומר שהקבוצה {% equation %}\left\{ 1,\theta,\dots,\theta^{n-1},\theta\right\} {% endequation %} היא <strong>תלויה לינארית</strong> (יש בה {% equation %}n+1{% endequation %} איברים של המרחב הוקטורי {% equation %}F\left(\theta\right){% endequation %} מעל {% equation %}F{% endequation %}) והצירוף הלינארי שלה ששווה 0 יתן לנו פולינום שמאפס את {% equation %}\theta{% endequation %} ויוכיח ש-{% equation %}\theta{% endequation %} אלגברי.

אם כן, משפט ראשון שאפשר לצטט עוסק בקשר בין הרחבות פשוטות והרחבות סופיות:
<ul>
 	<li>הרחבה פשוטה {% equation %}F\left(\theta\right)/F{% endequation %} היא סופית אם ורק אם {% equation %}\theta{% endequation %} אלגברי מעל {% equation %}F{% endequation %}.</li>
</ul>
או באופן שקול:
<ul>
 	<li>הרחבה פשוטה {% equation %}F\left(\theta\right)/F{% endequation %} היא אינסופית אם ורק אם {% equation %}\theta{% endequation %} טרנסנדנטי מעל {% equation %}F{% endequation %}.</li>
</ul>
אם כן, ראינו שהרחבה פשוטה היא לפעמים סופית ולפעמים לא, אבל אנחנו יודעים בדיוק מה קורה בכל אחד מהמקרים. מה עם הכיוון השני? האם הרחבה סופית היא בהכרח פשוטה, או שאפשר לייצר הרחבות סופיות אחרות? אינטואיטיבית נראה לי מובן מאליו שאפשר לייצר הרחבות מתוחכמות שאי אפשר ליצור על ידי איבר בודד ועדיין לקבל מימד סופי מעל {% equation %}F{% endequation %}, ולכן כל כך מפתיע (אותי) לגלות ש"כמעט תמיד" מתקיים שאם {% equation %}E/F{% endequation %} הרחבה סופית אז היא גם פשוטה. התוצאה הזו נקראת <strong>משפט האיבר הפרימיטיבי</strong> והיא תצטרך לחכות להמשך כי הניסוח וההוכחה שלה דורשים מושגים שעדיין אין לנו. בכל זאת אצטט אותה:
<ul>
 	<li>אם {% equation %}E/F{% endequation %} הרחבה סופית וספרבילית, אז {% equation %}E/F{% endequation %} פשוטה.</li>
</ul>
אני לא יכול להסביר כרגע מה "ספרבילית" אומר, אבל מקרה פרטי של המשפט שלעיל הוא שאם {% equation %}E/F{% endequation %} הרחבה סופית ו-{% equation %}F{% endequation %} שדה ממציין 0 (כמו {% equation %}\mathbb{Q}{% endequation %}) אז {% equation %}E/F{% endequation %} תהיה פשוטה. כלומר, אם אנחנו רוצים למצוא הרחבה סופית שאינה פשוטה אנחנו נדחפים לשדות "מוזרים" עם מציין שונה מאפס, וגם שם המשפט יעבוד לפעמים.

מכך שכל הרחבה פשוטה עם איבר אלגברי היא סופית אפשר לקבל במהירות תוצאה נוספית:
<ul>
 	<li>אם {% equation %}E/F{% endequation %} הרחבה סופית, אז היא הרחבה אלגברית.</li>
</ul>
למה זה נכון? בואו ניקח {% equation %}\theta\in E{% endequation %} כלשהו. אנחנו רוצים להראות שהוא אלגברי מעל {% equation %}F{% endequation %}, וראינו כבר שזה שקול לכך ש-{% equation %}\left[F\left(\theta\right):F\right]{% endequation %} סופית. כעת, {% equation %}F\left(\theta\right){% endequation %} הוא תת-מרחב וקטורי של {% equation %}E{% endequation %}, כשחושבים על שני השדות הללו כמרחבים וקטוריים מעל {% equation %}F{% endequation %}. המימד של תת-מרחב קטן או שווה למימד של המרחב כולו, ולכן אם {% equation %}\left[E:F\right]{% endequation %} סופית, כך גם {% equation %}\left[F\left(\theta\right):F\right]{% endequation %}.

מה עם הכיוון השני של המשפט הזה? ובכן:
<ul>
 	<li>זה <strong>לא נכון</strong> שאם {% equation %}E/F{% endequation %} הרחבה אלגברית אז היא סופית.</li>
</ul>
האם אני יכול לתת דוגמא נגדית פשוטה לטענה הזו? לא בדיוק. אילו שדות אנחנו מכירים בשלב הזה? את {% equation %}\mathbb{Q},\mathbb{R},\mathbb{C}{% endequation %} והרחבות פשוטות שלהם. כעת, {% equation %}\left[\mathbb{C}:\mathbb{R}\right]=2{% endequation %} (כי הפולינום המינימלי של {% equation %}i{% endequation %} הוא {% equation %}x^{2}+1{% endequation %}) ובהמשך נראה ש-{% equation %}\mathbb{C}{% endequation %} לא ניתן להרחבה אלגברית שתניב משהו חדש, אז זה לא המקום לחפש בו הרחבות אלגבריות אינסופיות. כמו כן, {% equation %}\left[\mathbb{R}:\mathbb{Q}\right]{% endequation %} אינסופית אבל זו לא הרחבה אלגברית (כי למשל {% equation %}\pi{% endequation %} לא אלגברי מעל {% equation %}\mathbb{Q}{% endequation %}). אז מה כן אפשר לתת? בהמשך נראה שקיים יצור שנקרא <strong>הסגור האלגברי</strong> של {% equation %}\mathbb{Q}{% endequation %}; היצור הזה (שהוא ממש לא {% equation %}\mathbb{R}{% endequation %}) הוא הרחבה אלגברית של {% equation %}\mathbb{Q}{% endequation %} אבל הוא יהיה רחוק מלהיות הרחבה סופית.

אפיון קצת יותר מחודד למהי הרחבה סופית אפשר למצוא במשפט הבא:
<ul>
 	<li>הרחבה {% equation %}E/F{% endequation %} היא סופית אם ורק אם {% equation %}E{% endequation %} מתקבל מ-{% equation %}F{% endequation %} על ידי הוספת מספר <strong>סופי</strong> של איברים אלגבריים מעל {% equation %}F{% endequation %}.</li>
</ul>
איך מוכיחים את זה? אנחנו עוד לא שם, אבל נהיה עוד מעט.

ראינו את הקשר בין "הרחבה פשוטה" ו"הרחבה סופית" ואת הקשר בין "הרחבה סופית" ו"הרחבה אלגברית". ומה על הקשר בין הרחבות אלגבריות ופשוטות? ובכן, צד אחד הוא נכון:
<ul>
 	<li>כל הרחבה פשוטה על ידי איבר אלגברי היא אלגברית.</li>
</ul>
אינטואיטיבית, זה בגלל שב-{% equation %}F\left(\theta\right){% endequation %} האיברים הם רק אברי {% equation %}F{% endequation %} שאלגבריים באופן טריוויאלי (אם {% equation %}a\in F{% endequation %} אז {% equation %}x-a{% endequation %} הוא הפולינום המינימלי של {% equation %}a{% endequation %} מעל {% equation %}F{% endequation %}) ו-{% equation %}\theta{% endequation %} אלגברי על פי ההנחה (כמובן שאם {% equation %}\theta{% endequation %} היה טרנסנדנטי אז ההרחבה לא הייתה אלגברית). עדיין, יש פה משהו קצת לא ברור - למה אם {% equation %}\theta{% endequation %} אלגברי זה אומר שגם כל החזקות שלו אלגבריות? וכל הפולינומים ב-{% equation %}\theta{% endequation %} אלגבריים? למשל, למה {% equation %}\theta^{7}+3\theta+2{% endequation %} אלגברי? השאלה הזו היא מקרה פרטי של שאלה כללית יותר: נניח ש-{% equation %}\alpha,\beta{% endequation %} הם שני איברים אלגבריים מעל {% equation %}F{% endequation %}. האם {% equation %}\alpha+\beta{% endequation %} אלגברי? והאם {% equation %}\alpha\beta{% endequation %} אלגברי? במילים אחרות, האם המספרים האלגבריים מעל {% equation %}F{% endequation %} הם <strong>חוג</strong>? זה מטפל בפולינומים ב-{% equation %}\theta{% endequation %} כי מהסגירות לכפל מקבלים גם ש-{% equation %}\theta^{n}{% endequation %} אלגברי וגם ש-{% equation %}a_{n}\theta^{n}{% endequation %} אלגברי עבור {% equation %}a_{n}\in F{% endequation %} (כל איבר של {% equation %}F{% endequation %} הוא אלגברי מעל {% equation %}F{% endequation %}) ומהסגירות לחיבור מקבלים את הפולינום כולו.

ובכן, בהמשך נראה שהמשפט הזה נכון, ואפילו יותר מכך: אם {% equation %}\alpha,\beta{% endequation %} אלגבריים מעל {% equation %}F{% endequation %} כך גם {% equation %}\alpha\pm\beta{% endequation %} ו-{% equation %}\alpha\beta{% endequation %} ואם {% equation %}\beta\ne0{% endequation %} אז גם {% equation %}\frac{\alpha}{\beta}{% endequation %}; במילים אחרות, אם ניקח הרחבה {% equation %}E/F{% endequation %}, אז אוסף כל האיברים ב-{% equation %}E{% endequation %} שהם אלגבריים מעל {% equation %}F{% endequation %} יהיה <strong>תת-שדה</strong> של {% equation %}F{% endequation %}. יכול להיות מפתה לנסות להוכיח את המשפט הזה כבר עכשיו - זה מרגיש שאמורה להיות לו הוכחה קונסטרוקטיבית - ניקח פולינומים שמאפסים את {% equation %}\alpha,\beta{% endequation %} ונבנה מהם איכשהו פולינום שמאפס את {% equation %}\alpha+\beta{% endequation %}. אני לא אומר שאי אפשר לעשות את זה, אבל זה יהיה כרוך בקושי טכני; אני עוד מעט הולך להוכיח ממילא משפט שההוכחה שלו אכן תהיה כרוכה בקושי טכני, והטענה שלי תתקבל ממנו כמסקנה פשוטה יחסית, כך שאין סיבה לחזור על הקושי הטכני פעמיים.

נסכם: ראינו שאם {% equation %}\theta{% endequation %} אלגברי מעל {% equation %}F{% endequation %} אז ההרחבה הפשוטה {% equation %}F\left(\theta\right){% endequation %} היא אלגברית. מה עם הכיוון השני? אם {% equation %}E/F{% endequation %} הרחבה אלגברית, האם היא פשוטה? ובכן, לא. אם זו הרחבה אינסופית (ויש הרחבות אלגבריות אינסופיות) אז בוודאי שאינה פשוטה (ראינו קודם שכל הרחבה אלגברית פשוטה היא סופית). אם לעומת זאת ההרחבה סופית, אז משפט האיבר הפרימיטיבי שהזכרתי קודם נכנס לתמונה ומראה שבחלק מהמקרים (כאשר {% equation %}E/F{% endequation %} הרחבה <strong>ספרבילית</strong>, מה שזה לא יהיה) אז {% equation %}E/F{% endequation %} פשוטה.
<h2>בואו נרחיב על הרחבות</h2>
כל הדיון עד כה התייחס לסיטואציה הפשוטה יחסית של הרחבה בודדת {% equation %}E/F{% endequation %}. הסיפור נעשה מעניין באמת כשיש לנו יותר מהרחבה אחת במשחק בו זמנית. המקרה המעניין הפשוט ביותר הוא זה שבו יש לנו <strong>שלושה</strong> שדות שכל אחד מרחיב את קודמו: הרחבות {% equation %}E/F{% endequation %} ו-{% equation %}K/E{% endequation %}. מכיוון ש-{% equation %}F\subseteq E\subseteq K{% endequation %} הרי שגם יש לנו פה הרחבה {% equation %}K/F{% endequation %}, ו-{% equation %}E{% endequation %} הוא מעין "שדה ביניים" של ההרחבה {% equation %}K/F{% endequation %} הזו. לדבר הזה אני אקרא לרוב <strong>מגדל של שדות</strong>.

השאלה הראשונה לטפל בה היא זו: אילו דברים מעניינים אפשר לומר על {% equation %}K/F{% endequation %} אם אנחנו כבר יודעים דברים מעניינים על {% equation %}E/F{% endequation %} ועל {% equation %}K/E{% endequation %}? למשל, אם שתיהן סופיות, האם גם {% equation %}K/F{% endequation %} סופית? לא רק שהתשובה היא "כן", אלא גם אנחנו יודעים בדיוק <strong>כמה</strong> היא סופית, וה<strong>כמה</strong> הזה יהיה שימושי בצורה בלתי רגילה. הנה המשפט:
<ul>
 	<li>אם {% equation %}F\subseteq E\subseteq K{% endequation %} שדות אז {% equation %}\left[K:F\right]=\left[K:E\right]\left[E:F\right]{% endequation %}</li>
</ul>
במילים: המימד של המרחב הוקטורי {% equation %}K{% endequation %} מעל השדה {% equation %}F{% endequation %} הוא מכפלת המימדים של המרחב הוקטורי {% equation %}E{% endequation %} מעל {% equation %}F{% endequation %} והמרחב הוקטורי {% equation %}K{% endequation %} מעל {% equation %}E{% endequation %}. שימו לב: יש לנו פה שני מרחבים וקטוריים שונים <strong>מעל שדות שונים</strong>. זו סיטואציה שונה ממה שקורה בדרך כלל באלגברה לינארית, שם קובעים את השדה מראש וכל הדיון מתנהל מעליו; פה יש לנו מראש אינטראקציה בין מרחבים שהם מעל שדות שונים וקשורים זה לזה.

ההוכחה של המשפט היא טכנית (זה המשפט הטכני שדיברתי עליו קודם) אבל די אינטואיטיבית. בואו ניקח בסיסים לשני המרחבים הוקטוריים שלנו: {% equation %}\left\{ \alpha_{1},\dots,\alpha_{n}\right\} {% endequation %} יהיה בסיס למרחב הוקטורי {% equation %}E{% endequation %} מעל {% equation %}F{% endequation %}, ואילו {% equation %}\left\{ \beta_{1},\dots,\beta_{m}\right\} {% endequation %} יהיה בסיס למרחב הוקטורי {% equation %}K{% endequation %} מעל {% equation %}E{% endequation %}. נראה מתבקש מאוד שהבסיס ל-{% equation %}K{% endequation %} מעל {% equation %}F{% endequation %} יהיה פשוט מורכב מכל המכפלות האפשריות: {% equation %}B=\left\{ \alpha_{i}\beta_{j}\ |\ 1\le i\le n,1\le j\le m\right\} {% endequation %}. זו קבוצה מגודל {% equation %}mn=\left[K:E\right]\left[E:F\right]{% endequation %}, אז אם נוכיח שהיא אכן בסיס, סיימנו.

נתחיל מכך שהקבוצה שלנו אכן פורשת את {% equation %}K{% endequation %} מעל {% equation %}F{% endequation %}. ניקח {% equation %}\theta\in K{% endequation %} כלשהו. אז מכיוון שה-{% equation %}\beta{% endequation %}-ות הן בסיס ל-{% equation %}K{% endequation %} מעל {% equation %}E{% endequation %}, נקבל:

{% equation %}\theta=\sum_{j=1}^{m}b_{j}\beta_{j}{% endequation %}

כך ש-{% equation %}b_{1},\dots,b_{m}\in E{% endequation %} איברים כלשהם. כעת, כל אחד מהאיברים הללו ניתן לכתיבה בעצמו בתור צירוף לינארי של ה-{% equation %}\alpha{% endequation %}-ות שמהוות בסיס ל-{% equation %}E{% endequation %} מעל {% equation %}F{% endequation %}, כך שנקבל:

{% equation %}b_{j}=\sum_{i=1}^{n}a_{i}^{j}\alpha_{i}{% endequation %}

עבור {% equation %}a_{i}^{j}\in F{% endequation %}-ים לכל {% equation %}1\le i\le n,1\le j\le m{% endequation %}.

משתי המשוואות הללו ביחד מקבלים:

{% equation %}\theta=\sum_{j=1}^{m}\left(\sum_{i=1}^{n}a_{i}^{j}\alpha_{i}\right)\beta_{j}=\sum_{i,j}a_{i}^{j}\left(\alpha_{i}\beta_{j}\right){% endequation %}

וזה צירוף לינארי עם מקדמים מ-{% equation %}F{% endequation %} של אברי הקבוצה {% equation %}B{% endequation %} שלנו. מכאן שהיא אכן קבוצה פורשת.

נשאר עדיין להראות ש-{% equation %}B{% endequation %} היא קבוצה בלתי תלויה לינארית; הדרך הפשוטה לעשות זאת היא לקחת צירוף לינארי של אבריה ששווה אפס ולהראות שכל מקדם בצירוף הוא אפס. אם כן, נניח ש-

{% equation %}\sum_{i,j}a_{i}^{j}\left(\alpha_{i}\beta_{j}\right)=0{% endequation %}

אז בואו "נהפוך" את המשוואה הזו; נקבץ מקדמים של כל {% equation %}\beta_{j}{% endequation %} ונקבל

{% equation %}\sum_{j=1}^{m}\left(\sum_{i=1}^{n}a_{i}^{j}\alpha_{i}\right)\beta_{j}=0{% endequation %}

קיבלנו כאן צירוף לינארי של אברי <strong>בסיס</strong> של {% equation %}K{% endequation %} מעל {% equation %}E{% endequation %} ששווה אפס, לכן נקבל לכל {% equation %}1\le j\le m{% endequation %} את המשוואה

{% equation %}\sum_{i=1}^{n}a_{i}^{j}\alpha_{i}=0{% endequation %}

וזה צירוף לינארי של אברי <strong>בסיס</strong> של {% equation %}E{% endequation %} מעל {% equation %}F{% endequation %} ולכן {% equation %}a_{i}^{j}=0{% endequation %} לכל {% equation %}1\le i\le n{% endequation %} וכל {% equation %}1\le j\le m{% endequation %}, וקיבלנו את מה שרצינו - הקבוצה {% equation %}B{% endequation %} היא אכן בסיס ל-{% equation %}K{% endequation %} מעל {% equation %}F{% endequation %}. אין בהוכחה הזו שום דבר מתוחכם; סתם כתיבה טכנית בסגנון אלגברה לינארית.

לא סיימתי את ההוכחה עד הסוף, כי לא התייחסתי לאפשרות שאחת מההרחבות {% equation %}E/F{% endequation %} או {% equation %}K/E{% endequation %} היא <strong>אינסופית</strong>; במקרה זה גם {% equation %}K/F{% endequation %} תהיה אינסופית (מה שמתאים לתיאור המשפט בתור מכפלה, אם מקבלים את המוסכמה {% equation %}\infty\cdot a=\infty{% endequation %} וכדומה). אין כאן יותר מדי מה לומר: אם {% equation %}K/E{% endequation %} היא אינסופית אז יש לנו קבוצה אינסופית של אברי {% equation %}K{% endequation %} שהיא בלתי תלויה לינארית מעל {% equation %}E{% endequation %}; מכאן שבוודאי שהיא תהיה בלתי תלויה לינארית גם מעל {% equation %}F{% endequation %} (כי מעל {% equation %}F{% endequation %} יש <strong>פחות </strong>צירופים לינאריים אפשריים שיכולים לקלקל את תכונת ה"בלתי תלויה לינארית" שלה) ולכן {% equation %}K/F{% endequation %} אינסופית. אם לעומת זאת {% equation %}E/F{% endequation %} אינסופית, אז קיימת קבוצה אינסופית של אברי {% equation %}E{% endequation %} שהיא בלתי תלויה מעל {% equation %}F{% endequation %}; <strong>אותה קבוצה בדיוק</strong> היא כמובן גם קבוצה של אברי {% equation %}K{% endequation %} שהיא בלתי תלויה מעל {% equation %}F{% endequation %}, ולכן שוב {% equation %}K/F{% endequation %} אינסופית.

מכאן ואילך כל מה שיקרה בפוסט הזה יהיה תוצאה של המשפט שזה עתה הראיתי.

לפני שנטבע בים של משפטים כלליים, הנה דוגמא קטנה וחביבה שמראה כמה המשפט הזה יעיל.

בואו נסתכל על הפולינום {% equation %}p\left(x\right)=x^{3}-3x-1{% endequation %} מעל {% equation %}\mathbb{Q}{% endequation %}. אפשר לראות בעזרת "משפט הניחוש האינטליגנטי" שאין לפולינום הזה שורשים מעל {% equation %}\mathbb{Q}{% endequation %} (פשוט בודקים את כל האפשרויות; המשפט מצביע על כולן, ויש מספר סופי מהן) ולכן, מכיוון שהוא ממעלה 3, הוא אי-פריק. יהא {% equation %}\alpha{% endequation %} שורש שלו (בפוסט הקודם ראינו שקיים כזה) ונסתכל על השדה {% equation %}\mathbb{Q}\left(\alpha\right){% endequation %}. השאלה: האם {% equation %}\sqrt{2}\in\mathbb{Q}\left(\alpha\right){% endequation %}?

נסו רגע לחשוב איך אפשר להוכיח טענה כזו בלי כל מה שראינו בפוסט הזה. התשובה שלי: אין לי מושג. אני מניח שהייתי מנסה למצוא הצגה מפורשת ל-{% equation %}\alpha{% endequation %} בעזרת נוסחת השורשים לפולינום ממעלה שלישית (אוי ווי לי) ואז... אה... אולי הייתי כופל... אה... אולי הייתי מסתכל על פולינום בזה... אה... בחיי שאין לי מושג, וכל מה שאני מנסה לחשוב עליו רק מפיל אותי לים טכני מזעזע.

ועם מה שראינו?

ובכן, אם {% equation %}\sqrt{2}\in\mathbb{Q}\left(\alpha\right){% endequation %} אז קיבלנו מגדל של שדות: {% equation %}\mathbb{Q}\subseteq\mathbb{Q}\left(\sqrt{2}\right)\subseteq\mathbb{Q}\left(\alpha\right){% endequation %}. בפרט אנחנו צריכים לקבל ש-{% equation %}\left[\mathbb{Q}\left(\sqrt{2}\right):\mathbb{Q}\right]{% endequation %} צריך לחלק את {% equation %}\left[\mathbb{Q}\left(\alpha\right):\mathbb{Q}\right]{% endequation %}. אלא מה? הפולינום המינימלי של {% equation %}\sqrt{2}{% endequation %} מעל {% equation %}\mathbb{Q}{% endequation %} הוא {% equation %}x^{2}-2{% endequation %} ולכן {% equation %}\left[\mathbb{Q}\left(\sqrt{2}\right):\mathbb{Q}\right]=2{% endequation %}, ואילו הפולינום המינימלי של {% equation %}\alpha{% endequation %} מעל {% equation %}\mathbb{Q}{% endequation %} הוא {% equation %}x^{3}-3x-1{% endequation %} ולכן {% equation %}\left[\mathbb{Q}\left(\alpha\right):\mathbb{Q}\right]=3{% endequation %} אבל 2 לא מחלק את 3 - והופס, הסיפור נגמר. איכשהו הפכנו את השאלה המורכבת "האם ניתן להציג איבר באמצעות פעולות החיבור, החיסור, הכפל והחילוק של איברים אחרים" לשאלה הפשוטה "האם מספר טבעי אחד מחלק מספר טבעי אחר". לדבר הזה יש לי שם אחד ויחיד - <strong>קסם</strong>.
<h2>פשוט על פשוט, אלגברי על אלגברי</h2>
בואו ניקח הרחבה {% equation %}E/F{% endequation %} ושני איברים {% equation %}\alpha,\beta\in E{% endequation %}. קודם דיברנו על "הרחבה פשוטה" של {% equation %}F{% endequation %} - השדה {% equation %}F\left(\alpha\right){% endequation %} שמתקבל מ"הוספת" {% equation %}\alpha{% endequation %} ו"סגירה" ביחס לכך. פורמלית ההגדרה שלנו הייתה קצת שונה: הגדרנו את {% equation %}F\left(\alpha\right){% endequation %} בתור השדה הקטן ביותר שמכיל גם את {% equation %}F{% endequation %} וגם את {% equation %}\alpha{% endequation %}; הוכחנו ששדה כזה קיים כי הוא שווה לחיתוך כל השדות שמכילים את {% equation %}F{% endequation %} ואת {% equation %}\alpha{% endequation %} - חיתוך שלכל הפחות {% equation %}E{% endequation %} עצמו משתתף בו ולכן הוא מוגדר היטב.

את אותו דבר בדיוק אפשר לעשות גם עבור שני איברים: להגדיר את {% equation %}F\left(\alpha,\beta\right){% endequation %} בתור השדה הקטן ביותר שמכיל את {% equation %}\alpha,\beta{% endequation %} ואת {% equation %}F{% endequation %}. השאלה שמייד קופצת באופן טבעי היא האם מתקיים {% equation %}F\left(\alpha,\beta\right)=F\left(\alpha\right)\left(\beta\right){% endequation %}. כלומר, האם השדה {% equation %}F\left(\alpha,\beta\right){% endequation %} שווה ממש לשדה שמתקבל על ידי כך שקודם מרחיבים את {% equation %}F{% endequation %} בצורה פשוטה עם {% equation %}\alpha{% endequation %} ואז את השדה שהתקבל מרחיבים בצורה פשוטה עם {% equation %}\beta{% endequation %}.

התשובה חיובית. מצד אחד {% equation %}F\left(\alpha\right)\left(\beta\right){% endequation %} הוא שדה שמכיל גם את {% equation %}F{% endequation %}, גם את {% equation %}\alpha{% endequation %} וגם את {% equation %}\beta{% endequation %} ולכן על פי ההגדרה {% equation %}F\left(\alpha,\beta\right){% endequation %} מוכל בו. מצד שני, {% equation %}F\left(\alpha,\beta\right){% endequation %} הוא שדה שמכיל את {% equation %}F{% endequation %} ואת {% equation %}\alpha{% endequation %} ולכן בפרט מכיל את כל {% equation %}F\left(\alpha\right){% endequation %}; על כן, הוא שדה שמכיל את כל {% equation %}F\left(\alpha\right){% endequation %} וגם את {% equation %}\beta{% endequation %} ולכן מכיל גם את {% equation %}F\left(\alpha\right)\left(\beta\right){% endequation %}. קיבלנו ששני השדות אכן שווים; לא היה פה משהו מפתיע במיוחד.

אם זה עובד עם שני איברים, אין סיבה שלא יעבוד עם מספר סופי כלשהו של איברים (בואו לא נדבר על אינסוף איברים כרגע...). אם {% equation %}\alpha_{1},\dots,\alpha_{n}\in E{% endequation %} אז {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %} מוגדר בתור השדה הקטן ביותר שמכיל את {% equation %}F{% endequation %} ואת האיברים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %}, ויוצא שהוא שווה לסדרת ההרחבות הפשוטות {% equation %}F\left(\alpha_{1}\right)\left(\alpha_{2}\right)\cdots\left(\alpha_{n}\right){% endequation %}. פורמלית, אפשר לסמן {% equation %}F_{0}=F{% endequation %} ו-{% equation %}F_{k+1}=F_{k}\left(\alpha_{k+1}\right){% endequation %}, ולקבל מגדל של שדות

{% equation %}F=F_{0}\subseteq F_{1}\subseteq\dots\subseteq F_{n}=F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %}

האם אפשר לומר משהו מעניין על {% equation %}\left[F\left(\alpha_{1},\dots,\alpha_{n}\right):F\right]{% endequation %}? כן ולא. לא, במובן זה שאי אפשר לדעת במדויק מה המימד הזה יהיה, כי זה תלוי ביחסים בין האיברים שאיתם מרחיבים את {% equation %}F{% endequation %} ולא רק בקשר שלהם ל-{% equation %}F{% endequation %} עצמו, אבל עדיין אפשר לומר <strong>משהו</strong>. בואו נסמן {% equation %}\left[F\left(\alpha_{k}\right):F\right]=m_{k}{% endequation %} - זו מעלת הפולינום המינימלי של {% equation %}\alpha_{k}{% endequation %} מעל {% equation %}F{% endequation %}. כעת, {% equation %}F_{k}=F_{k-1}\left(\alpha_{k}\right)/F_{k-1}{% endequation %}, ולכן המימד של ההרחבה הזו שווה למעלת הפולינום המינימלי של {% equation %}\alpha_{k}{% endequation %} מעל {% equation %}F_{k-1}{% endequation %}. מכיוון ש-{% equation %}F\subseteq F_{k-1}{% endequation %}, הפולינום המינימלי של {% equation %}\alpha_{k}{% endequation %} יכול להיות רק <strong>קטן יותר</strong> מעל {% equation %}F_{k-1}{% endequation %}, כי הוא יהיה חייב לחלק את מי שהיה הפולינום המינימלי של {% equation %}\alpha_{k}{% endequation %} מעל {% equation %}F{% endequation %}. לכן {% equation %}\left[F_{k-1}\left(\alpha_{k}\right):F_{k-1}\right]\le m_{k}{% endequation %} ולכן נקבל:

{% equation %}\left[F\left(\alpha_{1},\dots,\alpha_{n}\right):F\right]=\left[F_{n}:F_{n-1}\right]\cdots\left[F_{1}:F_{0}\right]\le m_{n}\cdots m_{1}{% endequation %}

כלומר, יש לנו חסם עליון על מה מימד ההרחבה הזה יכול להיות; לא ערך מדויק כמו קודם. למשל, אפשר להראות ש-{% equation %}\left[\mathbb{Q}\left(\sqrt{2},\sqrt{3}\right):\mathbb{Q}\right]=4{% endequation %} אבל {% equation %}\left[\mathbb{Q}\left(\sqrt{2},-\sqrt{2}\right):\mathbb{Q}\right]=2{% endequation %}; זה נובע מכך ש-{% equation %}\sqrt{2},\sqrt{3}{% endequation %} הם איברים ש"לא קשורים אלגברית" אחד לשני, בעוד ש-{% equation %}-\sqrt{2}{% endequation %} מתקבל מ-{% equation %}\sqrt{2}{% endequation %} פשוט על ידי כפל באיבר מ-{% equation %}\mathbb{Q}{% endequation %}.

נסכם: ראינו קודם שהרחבה פשוטה עם איבר אלגברי היא סופית; עכשיו אנחנו רואים משהו קצת יותר כללי:
<ul>
 	<li>הרחבה {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right)/F{% endequation %} הנוצרת על ידי מספר סופי של איברים אלגבריים היא סופית.</li>
</ul>
הטענה הפשוטה הזו גם נותנת לנו את מה שנראה מסובך למדי קודם: המשפט שאם {% equation %}E/F{% endequation %} היא הרחבה ו-{% equation %}\alpha,\beta\in E{% endequation %} הם אלגבריים מעל {% equation %}F{% endequation %}, אז גם האיברים {% equation %}\alpha\pm\beta{% endequation %}, {% equation %}\alpha\beta{% endequation %} ועבור {% equation %}\beta\ne0{% endequation %} גם {% equation %}\frac{\alpha}{\beta}{% endequation %} הם כולם אלגבריים מעל {% equation %}F{% endequation %}. זה נובע מכך שכל האיברים הללו הם בעצמם איברים של ההרחבה {% equation %}F\left(\alpha,\beta\right){% endequation %} שהיא סופית ולכן אלגברית.

ראינו את ההכללה של המשפט "כל הרחבה פשוטה היא סופית". כעת, ההיפוך של המשפט הזה - "כל הרחבה סופית היא פשוטה" - לא היה נכון, אם כי משפט האיבר הפרימיטיבי מראה שהוא כן נכון במקרים רבים; אבל עבור המשפט המורחב שכרגע הצגתי ההפך כן נכון:
<ul>
 	<li>אם הרחבה {% equation %}E/F{% endequation %} היא סופית אז {% equation %}E=F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %} עבור איברים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} אלגבריים מעל {% equation %}F{% endequation %}.</li>
</ul>
כלומר, כל הרחבה סופית נוצרת על ידי <strong>מספר סופי</strong> של איברים אלגבריים. ההוכחה לכך היא פשוטה למדי: אם {% equation %}E/F{% endequation %} היא סופית, זה אומר שקיים ל-{% equation %}E{% endequation %} בסיס מעל {% equation %}F{% endequation %}, נסמן את איבריו {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %}. מכיוון שכל איבר ב-{% equation %}E{% endequation %} ניתן לכתיבה בתור צירוף לינארי של האיברים הללו עם מקדמים מתוך {% equation %}F{% endequation %} ברור ש-{% equation %}E\subseteq F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %}, אבל מצד שני מכיוון ש-{% equation %}E{% endequation %} הוא מלכתחילה שדה שמכיל את {% equation %}F{% endequation %} ואת האיברים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} אז {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right)\subseteq E{% endequation %} ובסך הכל קיבלנו {% equation %}E=F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %}. רק נשאר להסביר למה כל {% equation %}\alpha_{i}{% endequation %} שכזה הוא אלגברי, וזה נובע מיידית מכך שההרחבה סופית: אם נסתכל על המגדל {% equation %}F\subseteq F\left(\alpha_{i}\right)\subseteq E{% endequation %} נקבל ש-{% equation %}\left[F\left(\alpha_{i}\right):F\right]{% endequation %} מחלק את {% equation %}\left[E:F\right]{% endequation %} ולכן {% equation %}\left[F\left(\alpha_{i}\right):F\right]{% endequation %} סופי בעצמו, אבל ראינו כבר בתחילת הפוסט שהרחבה <strong>פשוטה </strong>היא סופית אם ורק אם {% equation %}\alpha_{i}{% endequation %} אלגברי.

לסיום סדרת המשפטים הארוכה הזו נדבר על החור היחיד שנשאר פה: הרחבה אלגברית של הרחבה אלגברית. אני אוכיח שאם {% equation %}E/F{% endequation %} אלגברית ו-{% equation %}K/E{% endequation %} אלגברית אז גם {% equation %}K/F{% endequation %} אלגברית. כשלמדתי את הנושא הזה, המשפט הזה הפיל אותי בכל פעם מחדש; פשוט לא הצלחתי לזכור איך מוכיחים אותו. גם עכשיו אני לא זוכר. אני אומר לעצמי - המממ, ניקח {% equation %}\alpha\in K{% endequation %}. אני צריך למצוא פולינום מעל {% equation %}F{% endequation %} שמאפס אותו, אבל אין לי שום דבר כזה כרגע; מה שאני כן יודע הוא ש-{% equation %}K/E{% endequation %} אלגברית, אז קיים פולינום {% equation %}p\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %} כך ש-{% equation %}p\left(\alpha\right)=0{% endequation %}, ו-{% equation %}a_{0},\dots,a_{n}\in E{% endequation %}. עכשיו... אה... אני אמיר את המקדמים במשהו מעל {% equation %}F{% endequation %}... אה... כי הם אלגבריים... קיימים להם פולינומים... משהו משהו.... אה...

הבנתם את הרעיון. אין לי מושג. ושוב, זה לא במקרה. תורת השדות עושה <strong>קסמים</strong>, ומי שלא מכיר את הקסמים מנסה ללכת בדרך הישירה ונתקע עם הראש בקיר. צריך לאמץ חשיבה קצת שונה כדי להתמודד עם הבעיות שתורת השדות מציבה, וזה בדיוק סוד הכוח שלה והסיבה שהיא פתרה בעיות שהיו פתוחות מאות ואלפי שנים.

אז מה עושים? פשוט מאוד. האובייקט המרכזי בתורת השדות הוא הרחבות, אז בואו נייצר לעצמנו את ההרחבה הרלוונטית: נתבונן על {% equation %}F\left(\alpha,a_{0},\dots,a_{n}\right){% endequation %} - ההרחבה של {% equation %}F{% endequation %} שמתקבלת מכך שמוסיפים ל-{% equation %}F{% endequation %} את האיבר {% equation %}\alpha{% endequation %} שאנחנו רוצים להוכיח שהוא אלגברי מעל {% equation %}F{% endequation %}, ובנוסף את המקדמים של הפולינום שמאפס אותו מעל {% equation %}K{% endequation %}. עכשיו יש לנו מגדל של הרחבות:

{% equation %}F\subseteq F\left(a_{0},\dots,a_{n}\right)\subseteq F\left(\alpha,a_{0},\dots,a_{n}\right){% endequation %}

ההרחבה {% equation %}F\left(a_{0},\dots,a_{n}\right)/F{% endequation %} נוצרת על ידי מספר סופי של איברים <strong>אלגבריים</strong> מעל {% equation %}F{% endequation %}, ולכן כפי שראינו קודם, היא סופית.

ההרחבה {% equation %}F\left(\alpha,a_{0},\dots,a_{n}\right)/F\left(a_{0},\dots,a_{n}\right){% endequation %} היא הרחבה <strong>פשוטה</strong> שנוצרת על ידי הוספת {% equation %}\alpha{% endequation %} לשדה {% equation %}F\left(a_{0},\dots,a_{n}\right){% endequation %}. הנקודה היא ש-{% equation %}\alpha{% endequation %} הוא אלגברי מעל השדה הזה, כי כך בדיוק בנינו את השדה הזה! השדה {% equation %}F\left(a_{0},\dots,a_{n}\right){% endequation %} הוא בדיוק "{% equation %}F{% endequation %} ובנוסף לכך האיברים הספציפיים מתוך {% equation %}E{% endequation %} שנדרשים לנו כדי לקבל ש-{% equation %}\alpha{% endequation %} אלגברי". אם כן, גם ההרחבה הזו סופית, ולכן מהמשפט על המימד של מגדל הרחבות, אנחנו מקבלים שגם ההרחבה {% equation %}F\left(\alpha,a_{0},\dots,a_{n}\right)/F{% endequation %} סופית, והרחבה סופית היא אלגברית, ומכאן שבפרט {% equation %}\alpha{% endequation %} אלגברי מעל {% equation %}F{% endequation %}. שימו לב: בשום שלב לא הראיתי "בבת אחת" ש-{% equation %}K/F{% endequation %} אלגברית; לקחתי איבר בודד של {% equation %}K{% endequation %} והראיתי, בעזרת הרחבות שהיו תפורות סביב האיבר הזה, שהאיבר הוא אלגברי; זה מספיק.

זה מסיים את משפטי הבסיס שרציתי להראות, ואנחנו יכולים לעצור ולנשום אוויר וליהנות קצת עם האופן שבו המשפט {% equation %}\left[K:F\right]=\left[K:E\right]\left[E:F\right]{% endequation %} פותר כמעט לבדו את תעלומת הבניות בסרגל ומחוגה של היוונים; מכיוון שזה נושא שעומד לא רע בפני עצמו, אני אשמור את כולו לפוסט הבא.
