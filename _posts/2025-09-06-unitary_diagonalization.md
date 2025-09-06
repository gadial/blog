---
title: "לכסון אוניטרי"
layout: post
categories:
  - אלגברה לינארית
tags:
  - לכסון אוניטרי
  - טרנספורמציה נורמלית
  - מטריצה נורמלית
---


<h2>מבוא</h2>

אני רוצה לטפל בפוסט הזה בחוב בן 12 שנים שיש לי בבלוג. בשעתו כתבתי סדרת פוסטים באלגברה לינארית <a href="https://gadial.net/2013/04/27/adjoint_unitary_hermitian_matrices/">שהאחרון שבהם</a> הסתיים בהבטחה שאדבר על <strong>לכסון אוניטרי</strong> ואז... פשוט לא כתבתי את הפוסט הזה? לא בטוח למה שכחתי, אבל עכשיו זה בהחלט זמן טוב לחזור לזה אז יאללה, בואו נראה את זה. זו תוצאה ממש נחמדה.

אני <strong>לא</strong> אזכיר את כל הקונטקסט - בשביל זה יש את סדרת הפוסטים שלי באלגברה לינארית - אבל בכל זאת בואו נתחיל עם תזכורת קטנה שאפשר לדלג מעליה מה אנחנו עושים כאן בכלל.

ה"עולם" שלנו הוא מרחב וקטורי {% equation %}V{% endequation %} ממימד סופי, שהוא בנוסף גם <strong>מרחב מכפלה פנימית</strong> (אני מסמן את המכפלה הפנימית ב-{% equation %}\left\langle u,v\right\rangle {% endequation %}). זה אומר שהמרחב הוא מעל הממשיים {% equation %}\mathbb{R}{% endequation %} או מעל המרוכבים {% equation %}\mathbb{C}{% endequation %} - ובפוסט הזה שני המקרים הללו לא יהיו זהים. בפוסטים הקודמים בסדרה ראינו את המושג של אופרטור<strong> צמוד הרמיטית</strong>: אם {% equation %}T:V\to V{% endequation %} היה אופרטור מעל {% equation %}V{% endequation %}, אז הראינו שקיים ויחיד אופרטור שמסומן {% equation %}T^{*}:V\to V{% endequation %}, שנקרא "הצמוד ההרמיטי" שלו (לרוב אני אוותר על ה"הרמיטי") כך שמתקיים {% equation %}\left\langle T\left(v\right),u\right\rangle =\left\langle v,T^{*}\left(u\right)\right\rangle {% endequation %} לכל {% equation %}v,u\in V{% endequation %}. בעזרת המושג הזה אפשר להגדיר עוד שני סוגים נחמדים במיוחד של אופרטורים:

<ul> <li>אופרטור {% equation %}T{% endequation %} הוא <strong>צמוד לעצמו</strong> אם {% equation %}T=T^{*}{% endequation %}.</li>


<li>אופרטור {% equation %}T{% endequation %} הוא <strong>אוניטרי</strong> אם {% equation %}T^{-1}=T^{*}{% endequation %}.</li>

</ul>

לפעמים משתמשים ב"הרמיטי" במקום "צמוד לעצמו", אבל אני מעדיף את צמוד לעצמו כי "הרמיטי" זה משהו שנהוג לומר רק כשאנחנו מעל {% equation %}\mathbb{C}{% endequation %} ואם אנחנו מעל {% equation %}\mathbb{R}{% endequation %} אומרים "סימטרי" ו"צמוד לעצמו" מכסה את שני המקרים בצורה נוחה.

אני מגדיר הגדרה דומה עבור מטריצות: אם {% equation %}A{% endequation %} היא מטריצה, אז {% equation %}A^{*}{% endequation %} מוגדרת להיות המטריצה שמתקבלת משילוב של שתי פעולות, <strong>שחלוף</strong> של {% equation %}A{% endequation %} (החלפת השורות בעמודות) ו<strong>הצמדה</strong> של הכניסות של {% equation %}A{% endequation %}, במובן הרגיל של הצמדה של מספרים מרוכבים שבו {% equation %}\overline{z}=\overline{a+bi}=a-bi{% endequation %}. במילים אחרות, {% equation %}A_{ij}^{*}=\overline{A_{ji}}{% endequation %}. עם ההגדרה הזו, מטריצה {% equation %}A{% endequation %} הוא הרמיטית אם {% equation %}A=A^{*}{% endequation %} והיא אוניטרית אם {% equation %}A^{-1}=A^{*}{% endequation %}.

דיברנו על אופרטורים ומטריצות, בואו נדבר גם על וקטורים. כשיש לי מכפלה פנימית על מרחב, אני יכול להכניס לתמונה מושגים חדשים על וקטורים: <strong>אורך</strong> ו<strong>זווית</strong>. השימוש שלי בזווית כאן הוא פשוט: אני אומר ששני וקטורים {% equation %}u,v{% endequation %} הם <strong>אורתוגונליים</strong> ("ניצבים" - אינטואיטיבית, הם בזווית של 90 מעלות זה לזה) אם {% equation %}\left\langle u,v\right\rangle =0{% endequation %}. אני גם מסמן את <strong>הנורמה</strong> של וקטור ("האורך" שלו) ב-{% equation %}\|v\|=\sqrt{\left\langle v,v\right\rangle }{% endequation %}. מה שאוהבים מאוד באלגברה לינארית הם בסיסים <strong>אורתונורמליים</strong> של {% equation %}V{% endequation %}: בסיס {% equation %}\left\{ b_{1},\ldots,b_{n}\right\} {% endequation %} שהאיברים בו מקיימים {% equation %}\left\langle b_{i},b_{j}\right\rangle =\delta_{ij}=\begin{cases} 1 & i=j\\ 0 & i\ne j \end{cases}{% endequation %}, כלומר שכל האיברים בו הם מנורמה 1 ואורתוגונליים זה לזה. למה אלו בסיסים קסומים ונהדרים ונפלאים <a href="https://gadial.net/2012/02/06/inner_products_intro/">הסברתי בפעם אחרת</a>.

עכשיו, הנה קשר חמוד בין בסיסים אורתונורמליים ומטריצות אוניטריות. אם {% equation %}A{% endequation %} היא מטריצה אוניטרית מסדר {% equation %}n\times n{% endequation %}, כלומר {% equation %}A^{*}=A^{-1}{% endequation %}, אז בפרט {% equation %}A^{*}A=I{% endequation %}. בואו נסתכל על <strong>העמודות</strong> של {% equation %}A{% endequation %} בתור וקטורים מאורך {% equation %}n{% endequation %} ונסמן אותם {% equation %}v_{1},\ldots,v_{n}{% endequation %}. על פי ההגדרה של <a href="https://gadial.net/2011/10/06/matrix_product/">כפל מטריצות</a>, הכניסה ה-{% equation %}i,j{% endequation %} במכפלה {% equation %}A^{*}A{% endequation %} היא השורה ה-{% equation %}i{% endequation %} של {% equation %}A^{*}{% endequation %} שמוכפלת סקלרית בעמודה {% equation %}j{% endequation %} של {% equation %}A{% endequation %}. והשורה ה-{% equation %}i{% endequation %} של {% equation %}A^{*}{% endequation %} היא ההצמדה של העמודה ה-{% equation %}i{% endequation %} של {% equation %}A{% endequation %}, כלומר אנחנו מקבלים שהכניסה הזו שווה אל {% equation %}\sum_{k=1}^{n}\left[\overline{v_{i}}\right]_{k}\left[v_{j}\right]_{k}=\left\langle v_{j},v_{i}\right\rangle {% endequation %} ומכיוון שהמכפלה נותנת לנו את מטריצת היחידה {% equation %}I{% endequation %} קיבלנו ש-{% equation %}\left\langle v_{j},v_{i}\right\rangle =\delta_{i,j}{% endequation %}. במילים אחרות: <strong>העמודות של מטריצה אוניטרית הן בסיס אורתונורמלי </strong>(גם השורות, מאותו נימוק).

אוקיי, סיימנו עם התזכורת, בואו ניגש לאקשן!

<h2>מה זה לכסון אוניטרי?</h2>

כשמתחילים ללמוד אלגברה לינארית, המושג של <strong>לכסון</strong> הוא בדרך כלל אחד מהיעדים המרכזיים שמנסים להגיע אליהם. הרעיון הוא זה: אם יש לי מטריצה ריבועית {% equation %}A{% endequation %} מסדר {% equation %}n\times n{% endequation %}, אני רוצה למצוא מטריצה <strong>אלכסונית</strong> {% equation %}D{% endequation %} ש-{% equation %}A{% endequation %} דומה לה. "דמיון" פירושו שקיימת מטריצה הפיכה {% equation %}P{% endequation %} כך ש-{% equation %}P^{-1}AP=D{% endequation %}. זה לא בא משום מקום; אם {% equation %}A{% endequation %} מייצגת טרנספורמציה לינארית {% equation %}T{% endequation %} (במובן שאני מתאר <a href="https://gadial.net/2011/10/27/coordinates_transformations_matrices/">כאן</a>) אז דמיון אומר שגם {% equation %}D{% endequation %} מייצגת את {% equation %}T{% endequation %}, פשוט בבסיס אחר, ו-{% equation %}P{% endequation %} היא המטריצה שיודעת להעביר בין הבסיסים. אבל דמיון מטריצות הוא נחמד גם אם אין איזו טרנספורמציה לינארית ברקע; למשל, אם רוצים לחשב את החזקה של {% equation %}A{% endequation %} מהר, ואנחנו יודעים ש-{% equation %}A{% endequation %} דומה ל-{% equation %}D{% endequation %}, כלומר {% equation %}A=PDP^{-1}{% endequation %}, אז נשתמש בכך ש-{% equation %}A^{n}=\left(PDP^{-1}\right)\cdots\left(PDP^{-1}\right)=PD^{n}P^{-1}{% endequation %} (כל ה-{% equation %}P{% endequation %}-ים שבאמצע מבטלים זה את זה) ובכך שקל להעלות מטריצה אלכסונית בחזקה כלשהי (מעלים את האיברים על האלכסון בחזקה הזו) כדי לחשב מהר את החזקה של {% equation %}A{% endequation %}.

עכשיו, אם {% equation %}P^{-1}AP=D{% endequation %} זה אומר ש-{% equation %}AP=PD{% endequation %}. מה זה {% equation %}AP{% endequation %}? אפשר לחשוב על זה בתור מטריצה שהעמודות שלה הן התוצאה של כפל של {% equation %}A{% endequation %} בעמודות של {% equation %}P{% endequation %}. ואילו {% equation %}PD{% endequation %}, כאשר {% equation %}D{% endequation %} אלכסונית, זו מטריצה שהעמודות שלה הן כפל של העמודות של {% equation %}P{% endequation %} באיברים על האלכסון של {% equation %}D{% endequation %} (העמודה הראשונה כפול האיבר הראשון וכן הלאה). במילים אחרות, העמודות של {% equation %}P{% endequation %} הן וקטורים {% equation %}v_{i}{% endequation %} שמקיימים {% equation %}Av_{i}=\lambda_{i}v_{i}{% endequation %}. לוקטורים כאלו קוראים <strong>וקטורים עצמיים</strong> של {% equation %}A{% endequation %} ואילו {% equation %}\lambda_{i}{% endequation %} הם <strong>ערכים עצמיים</strong> ואני מניח שכולנו מכירים את זה כבר.

כאשר מלכסנים מטריצה, השיטה הבסיסית היא למצוא מהם הערכים העצמיים, בעזרת זה למצוא מהם הוקטורים העצמיים, ואז לבנות בעזרתם את {% equation %}P{% endequation %}. לרוע המזל, <strong>זה לא תמיד עובד</strong>. כדי שנוכל לקבל את {% equation %}P{% endequation %} אנחנו צריכים שיהיו לנו {% equation %}n{% endequation %} וקטורים עצמיים בלתי תלויים, במרחב ממימד {% equation %}n{% endequation %} - כלומר, אנחנו צריכים למצוא <strong>בסיס למרחב</strong> שיהיה מורכב כולו מוקטורים עצמיים של {% equation %}A{% endequation %}. לא תמיד יש כאלו, ואין קריטריון פשוט על {% equation %}A{% endequation %} שאומר לנו מתי זה עובד ("הריבוי הגאומטרי שווה לריבוי האלגברי" זה לא קריטריון פשוט).

אבל מה קורה עבור מרחבי מכפלה פנימית? כאן יש לנו מבנה נוסף על העולם, אולי זה מפשט את העניינים? ובכן, בערך: אם אנחנו מגדילים את הדרישה שלנו ורוצים לא סתם לכסון אלא לכסון שבו המטריצה המלכסנת היא <strong>אוניטרית</strong>, כלומר אם אנחנו לא רוצים סתם בסיס של וקטורים עצמיים אלא בסיס <strong>אורתונורמלי</strong> של וקטורים עצמיים, פתאום אנחנו מקבלים קריטריון מאוד קונקרטי ופשוט של אם ורק אם. זה משפט מרהיב לגמרי, והנה הוא:

<ul> <li>{% equation %}A{% endequation %} לכסינה אוניטרית ב-{% equation %}\mathbb{R}^{n}{% endequation %} אם ורק אם {% equation %}A=A^{*}{% endequation %}.</li>


<li>{% equation %}A{% endequation %} לכסינה אוניטרית ב-{% equation %}\mathbb{C}^{n}{% endequation %} אם ורק אם {% equation %}A^{*}A=AA^{*}{% endequation %}.</li>

</ul>

התכונה {% equation %}A=A^{*}{% endequation %} היא כזכור התכונה של להיות <strong>הרמיטי</strong>, אבל כשאנחנו מעל {% equation %}\mathbb{R}{% endequation %} כל פעולת ההצמדה לא עושה כלום, ולכן {% equation %}A=A^{*}{% endequation %} זו דרך אחרת לכתוב {% equation %}A=A^{t}{% endequation %} כש-{% equation %}t{% endequation %} מסמן את פעולת השחלוף של מטריצות, כלומר הדרישה היא ש-{% equation %}A{% endequation %} תהיה <strong>סימטרית</strong>.

הדרישה {% equation %}A^{*}A=AA^{*}{% endequation %} קצת פחות ברורה במבט ראשון. עוד רגע נראה מאיפה היא מגיעה, אבל עד כה לא היה לנו שם בשבילה, אז בואו נמציא אחד: נאמר ש-{% equation %}A{% endequation %} היא <strong>נורמלית</strong> אם {% equation %}A^{*}A=AA^{*}{% endequation %}. ניקח את השמות הללו גם עבור טרנספורמציות לינאריות, והנה לנו עוד ניסוח של המשפט:

<ul> <li>אם {% equation %}V{% endequation %} הוא מרחב מכפלה פנימית מעל {% equation %}\mathbb{R}{% endequation %} ו-{% equation %}T:V\to V{% endequation %} אז {% equation %}T{% endequation %} לכסינה אוניטרית אם ורק אם היא צמודה לעצמה.</li>


<li>אם {% equation %}V{% endequation %} הוא מרחב מכפלה פנימית מעל {% equation %}\mathbb{C}{% endequation %} ו-{% equation %}T:V\to V{% endequation %} אז {% equation %}T{% endequation %} לכסינה אוניטרית אם ורק אם היא נורמלית.</li>

</ul>

מאיפה התנאים הללו באים? להוכיח שהם <strong>הכרחיים</strong> זה קל. נניח שקיימת מטריצה אוניטרית {% equation %}U{% endequation %} (כלומר {% equation %}U^{*}=U^{-1}{% endequation %} - אני משתמש בזה הרבה עכשיו) כך ש-{% equation %}U^{*}AU=D{% endequation %} ו-{% equation %}D{% endequation %} היא מטריצה ריבועית. בואו נפעיל את אופרטור הכוכב על שני אגפי המשוואה - אני אשתמש פה בתכונות המוכרות שלו:

<ul> <li>{% equation %}\left(AB\right)^{*}=B^{*}A^{*}{% endequation %}</li>


<li>{% equation %}\left(A^{*}\right)^{*}=A{% endequation %}</li>

</ul>

אז על ידי הפעלה שלו על שני האגפים, אני מקבל {% equation %}U^{*}A^{*}U=\left(U^{*}AU\right)^{*}=D^{*}{% endequation %}. עכשיו, מכיוון ש-{% equation %}D{% endequation %} אלכסונית, זה אומר ש-{% equation %}D^{*}{% endequation %} היא כמו {% equation %}D{% endequation %} רק עם הצמדה של אברי האלכסון. אבל <strong>אם אנחנו מעל הממשיים</strong>, אז אברי האלכסון הם מספרים ממשיים, ולכן הצמדה שלהם לא משנה אותם ולכן <strong>במקרה הממשי</strong> מקבלים ש-{% equation %}D=D^{*}{% endequation %}, כלומר {% equation %}U^{*}AU=U^{*}A^{*}U{% endequation %}. נכפול משמאל ב-{% equation %}U{% endequation %} כדי לצמצם את ה-{% equation %}U^{*}{% endequation %} משם; נכפול מימין ב-{% equation %}U^{*}{% endequation %}, ונישאר עם {% equation %}A=A^{*}{% endequation %}, וזה בדיוק מה שרציתי להראות עבור המקרה הממשי.

עבור המקרה המרוכב בהחלט ייתכן ש-{% equation %}D\ne D^{*}{% endequation %}, אבל שתיהן הן עדיין מטריצות אלכסונית, ומטריצות אלכסוניות <strong>מתחלפות בכפל</strong>. נשתמש בזה כדי להראות ש-{% equation %}A,A^{*}{% endequation %} גם כן מתחלפות בכפל (זה די מתבקש מכך ש-{% equation %}A,A^{*}{% endequation %} ו-{% equation %}D,D^{*}{% endequation %} הם שני ייצוגים שונים לאותן טרנספורמציות, אבל בואו נראה את זה ברמת הפיפס הטכני בכל זאת). מהמשוואה {% equation %}U^{*}AU=D{% endequation %} נקבל {% equation %}A=UDU^{*}{% endequation %} ובדומה {% equation %}A^{*}=UD^{*}U^{*}{% endequation %}, וכעת:

{% equation %}A^{*}A=\left(UD^{*}U^{*}\right)\left(UDU^{*}\right)=UD^{*}\left(U^{*}U\right)DU^{*}=UD^{*}DU^{*}={% endequation %}

{% equation %}=UDD^{*}U^{*}=UD\left(U^{*}U\right)D^{*}U^{*}=\left(UDU^{*}\right)\left(UD^{*}U^{*}\right)=AA^{*}{% endequation %}

אז גם זה היה קל. האתגר שלנו יהיה להראות שהתנאים הללו הם גם <strong>מספיקים</strong>, כלומר אם הם מתקיימים באמת אפשר למצוא {% equation %}U{% endequation %} מופלאה שכזו.

<h2>לכסון אוניטרי של דברים צמודים לעצמם</h2>

מה שאני רוצה להראות עכשיו הוא שאם {% equation %}T:V\to V{% endequation %} היא טרנספורמציה צמודה לעצמה, כלומר {% equation %}T=T^{*}{% endequation %}, אז היא לכסינה אוניטרית. לכאורה אני צריך להסתפק במקרה שבו {% equation %}V{% endequation %} הוא מרחב מעל {% equation %}\mathbb{R}{% endequation %}, אבל ההוכחה תעבוד מעל {% equation %}\mathbb{C}{% endequation %} באותה מידה כי להיות הרמיטי זו תכונה חזקה למדי. פשוט, במקרה של {% equation %}\mathbb{C}{% endequation %} זה <strong>לא מספיק</strong>, יש עוד טרנספורמציות שאני צריך לטפל בהן.

ההוכחה היא באינדוקציה על המימד של {% equation %}V{% endequation %} (בפרט, אם {% equation %}V{% endequation %} הוא אינסוף ממדי שום דבר מזה לא יעבוד; <a href="https://gadial.net/2014/02/09/hilbert_spaces/">אלגברה לינארית מעל מרחב אינסוף ממדי</a> היא משחק שונה לגמרי). השלב הקריטי שלה הוא להראות של-{% equation %}T{% endequation %} קיים וקטור עצמי <strong>אחד</strong>; אחר כך אפשר לפצל את {% equation %}V{% endequation %} למרחב החד ממדי של "מה שהוקטור העצמי פורש" ולמרחב של "כל מה שניצב למרחב החד ממדי הזה", לעבוד באינדוקציה על המרחב הניצב הזה ואיכשהו להדביק את הכל בסוף עם סלוטייפ. אז השלב הראשון שלנו הוא להוכיח שיש ל-{% equation %}T{% endequation %} וקטור עצמי. בשביל זה אנחנו צריכים להזכיר לעצמנו מה עושים, טכנית, כדי למצוא וקטורים עצמיים.

אני לא אחזור על כל התהליך, אבל הרעיון הוא זה: לוקחים בסיס {% equation %}B{% endequation %} ל-{% equation %}V{% endequation %} ובונים את המטריצה {% equation %}A=\left[T\right]_{B}{% endequation %} שמייצגת את {% equation %}T{% endequation %} בבסיס {% equation %}B{% endequation %}. אין ממש חשיבות תיאורטית לשאלה איזה בסיס לוקחים - העיקר שאנחנו משיגים קונקרטיזציה שמעבירה מ-{% equation %}T{% endequation %} אל אוסף של מספרים בטבלה ("מטריצה"). עכשיו, מגדירים את הפולינום {% equation %}p\left(x\right)=\det\left(xI-A\right){% endequation %} שנקרא "הפולינום האופייני" של {% equation %}A{% endequation %}, מוצאים לו שורש {% equation %}\lambda{% endequation %}, ואז פותרים את מערכת המשוואות {% equation %}\left(\lambda I-A\right)x=0{% endequation %} - הפתרון שנקבל יהיה וקטור עצמי (ומובטח שיהיה פתרון אחד לפחות).

כל מה שתיארתי הוא טוב ויפה חוץ מעניין אחד: אמרתי ש"מוצאים שורש {% equation %}\lambda{% endequation %} לפולינום האופייני" - אבל מי מבטיח לנו ש<strong>קיים</strong> שורש? למשל, אם הפולינום האופייני הוא {% equation %}\lambda^{2}+1{% endequation %}, אז <strong>לא קיים לו שורש</strong>... מעל המספרים הממשיים, זאת אומרת. השורשים שלו הם {% equation %}\pm i{% endequation %} שהם מספרים מרוכבים. זו בדיוק הסיבה למה למטריצה

{% equation %}A=\left[\begin{array}{cc} 0 & 1\\ -1 & 0 \end{array}\right]{% endequation %}

שמתארת סיבוב ב-90 מעלות, אין וקטורים עצמיים ממשיים.

העניין הוא שזו בעיה שקיימת רק בממשיים. במרוכבים יש לנו את <strong>המשפט היסודי של האלגברה</strong> שמבטיח לנו שתמיד קיים שורש לכל פולינום (הוכחתי את זה <a href="https://gadial.net/2009/10/29/fundemental_theorem_of_algebra_algebraic_proof/">כאן</a>). כמובן, המקרה שמעניין אותנו הוא ספציפית זה של הממשיים, ולכן כן נצטרך להתאמץ יותר - עד עכשיו בטיעון שהצגתי בכלל לא השתמשנו בכך ש-{% equation %}T{% endequation %} צמודה לעצמה, וזה מן הסתם יצטרך לשחק תפקיד, והתפקיד הזה הוא פשוט למדי: אם {% equation %}T{% endequation %} היא צמודה לעצמה, אז כל הערכים העצמיים שלה הם <strong>ממשיים</strong>. זו טענה מרחיקת לכת שמעניינת הרבה יותר מאשר רק במסגרת ההוכחה הספציפית שלנו - למשל, בפיזיקה קוונטית משתמשים באופרטורים צמודים לעצמם כדי לתאר <strong>גדלים מדידים</strong> - המדידה על פי אופרטור מסוים מניבה ערך עצמי שלו, ולכן קריטי שהאופרטור יהיה צמוד לעצמו כי ערכים ממשיים הם הערכים שאנחנו "יודעים למדוד".

להוכיח את זה, זה קל. נניח של-{% equation %}T{% endequation %} יש ערך עצמי {% equation %}\lambda{% endequation %} עם וקטור עצמי {% equation %}v\ne0{% endequation %}, כלומר {% equation %}T\left(v\right)=\lambda v{% endequation %}, ועכשיו בואו נסתכל על הסקלר {% equation %}\lambda\left\langle v,v\right\rangle {% endequation %} ונשתמש בחוקי החשבון של מכפלות פנימיות ובכך ש-{% equation %}T{% endequation %} צמודה לעצמה:

{% equation %}\lambda\left\langle v,v\right\rangle =\left\langle \lambda v,v\right\rangle =\left\langle T\left(v\right),v\right\rangle ={% endequation %}

{% equation %}=\left\langle v,T\left(v\right)\right\rangle =\left\langle v,\lambda v\right\rangle =\overline{\lambda}\left\langle v,v\right\rangle {% endequation %}

מכיוון ש-{% equation %}v\ne0{% endequation %} אז {% equation %}\left\langle v,v\right\rangle >0{% endequation %} ואפשר לחלק בו ולקבל {% equation %}\lambda=\overline{\lambda}{% endequation %} - התכונה הזו שקולה לכך ש-{% equation %}\lambda\in\mathbb{R}{% endequation %}, אז סיימנו עם זה.

אם אני כבר בשוונג של הוכחות שהן משחק טכני עם המכפלה הפנימית, בואו גם נוכיח שוקטורים עצמיים שמתאימים לערכים עצמיים שונים של אופרטור צמוד לעצמו הם <strong>אורתוגונליים</strong>. כלומר נניח ש-{% equation %}T\left(v\right)=\lambda v{% endequation %} ו-{% equation %}T\left(u\right)=\rho u{% endequation %} עם {% equation %}\lambda\ne\rho{% endequation %} ונוכיח ש-{% equation %}\left\langle v,u\right\rangle =0{% endequation %}. בשביל לראות את זה, נסתכל הפעם על {% equation %}\lambda\left\langle v,u\right\rangle {% endequation %} ונשתמש פחות או יותר באותה סדרת מעברים:

{% equation %}\lambda\left\langle v,u\right\rangle =\left\langle \lambda v,u\right\rangle =\left\langle T\left(v\right),u\right\rangle ={% endequation %}

{% equation %}=\left\langle v,T\left(u\right)\right\rangle =\left\langle v,\rho u\right\rangle =\overline{\rho}\left\langle v,u\right\rangle {% endequation %}

מכיוון שהערכים העצמיים הם ממשיים אז {% equation %}\rho=\overline{\rho}{% endequation %} ולכן קיבלנו

{% equation %}\lambda\left\langle v,u\right\rangle =\rho\left\langle v,u\right\rangle {% endequation %}

נעביר אגפים:

{% equation %}\left(\lambda-\rho\right)\left\langle v,u\right\rangle =0{% endequation %}

ומכיוון ש-{% equation %}\lambda\ne\rho{% endequation %} החלק הזה במכפלה שונה מאפס, ולכן בהכרח {% equation %}\left\langle v,u\right\rangle =0{% endequation %}, מה שמסיים את החלק הזה של ההוכחה.

עכשיו נחזור לאתגר שלנו - להוכיח שלכל אופרטור צמוד לעצמו יש וקטור עצמי. יש לנו פה שני רעיונות שהשילוב של שניהם אמור לפתור את הבעיה:

<ol> <li>לכל אופרטור {% equation %}T:V\to V{% endequation %} כאשר {% equation %}V{% endequation %} הוא מעל המרוכבים קיים ערך עצמי {% equation %}\lambda{% endequation %} (מרוכב).</li>


<li>אם {% equation %}T{% endequation %} הוא צמוד לעצמו עם ערך עצמי {% equation %}\lambda{% endequation %}, אז {% equation %}\lambda{% endequation %} ממשי.</li>

</ol>

שני אלו באמת יפתרו את הבעיה, אבל צריך להדביק אותם בסלוטייפ והסלוטייפ יהיה קצת טכני. לב העניין הוא שאני לא יכול סתם כך להשתמש ב-1 כי נקודת המוצא שלי היא {% equation %}T:V\to V{% endequation %} כך ש-{% equation %}V{% endequation %} הוא מרחב וקטורי <strong>מעל הממשיים</strong> {% equation %}\mathbb{R}{% endequation %}.

אז בואו נתקדם בזהירות.

ראשית, אני אקח בסיס {% equation %}B{% endequation %} של {% equation %}V{% endequation %}, אבל לא סתם בסיס - <strong>בסיס אורתונורמלי</strong>. אני יודע בודאות שקיים כזה בסיס כי תהליך גרם-שמידט (שתיארתי <a href="https://gadial.net/2012/02/06/inner_products_intro/">כאן</a>) מבטיח את הקיום שלו. אבל למה אני צריך בסיס אורתונורמלי? כי עכשיו אני אגדיר מטריצה {% equation %}A=\left[T\right]_{B}{% endequation %} בדיוק כפי שתיארתי קודם, ואני צריך שגם המטריצה תהיה צמודה לעצמה, כלומר תקיים {% equation %}A^{*}=A{% endequation %}, ובשביל שזה יעבוד אני צריך שיתקיים {% equation %}A^{*}=\left[T^{*}\right]_{B}{% endequation %} ובשביל <strong>שזה</strong> יעבוד הבסיס צריך להיות אורתונורמלי. הראיתי את זה בפוסט <a href="https://gadial.net/2013/04/27/adjoint_unitary_hermitian_matrices/">הזה</a>.

עכשיו, {% equation %}A{% endequation %} היא מטריצה שהאיברים שלה לקוחים מתוך השדה שמעליו עובדים - במקרה שלנו, {% equation %}\mathbb{R}{% endequation %}. אבל שום דבר לא מונע מאיתנו להכניס לתמונה מרחב וקטורי <strong>חדש</strong>, מעל {% equation %}\mathbb{C}{% endequation %}, ולהשתמש בו ב-{% equation %}A{% endequation %} באותו אופן בדיוק כי היא גם מטריצה מעל {% equation %}\mathbb{C}{% endequation %}. אז נסתכל על המרחב {% equation %}\mathbb{C}^{n}{% endequation %}. מעל המרחב הזה, {% equation %}A{% endequation %} מגדירה אופרטור לינארי על ידי הפעולה {% equation %}A\left(v\right)=Av{% endequation %} (כופלים את המטריצה {% equation %}n\times n{% endequation %} שהיא {% equation %}A{% endequation %} בוקטור העמודה {% equation %}n\times1{% endequation %} שהוא {% equation %}v{% endequation %}, במובן הסטנדרטי של כפל מטריצה בוקטור). לכן קיים לאופרטור {% equation %}A{% endequation %} הזה ערך עצמי {% equation %}\lambda\in\mathbb{C}{% endequation %}. האם זה ערך עצמי <strong>ממשי</strong>? כן, <strong>בתנאי</strong> שהאופרטור {% equation %}A{% endequation %} הוא צמוד לעצמו. שמתם לב לניואנס? אני לא משתמש ישירות בזה ש-{% equation %}T{% endequation %} צמוד לעצמו, אלא צריך להראות שמכך נובע שהאופרטור {% equation %}A{% endequation %} שנגזר ממנו בדרך חתחתים של בחירה בבסיס אורתונורמלי, מציאת ייצוג ל-{% equation %}T{% endequation %} ואז <strong>החלפת שדה הבסיס</strong> ל-{% equation %}\mathbb{C}{% endequation %} - אחרי כל זה, האופרטור עדיין צמוד לעצמו. כן, זה לא משהו שקשה להראות, אבל הניואנס, הו, הניואנס.

בכל מקרה, בבסיס הסטנדרטי של {% equation %}\mathbb{C}^{n}{% endequation %} (זה שבו וקטורי הבסיס הם הוקטורים עם 1 בכניסה אחת ו-0 ביתר) ועם המכפלה הפנימית הסטנדרטית, המטריצה המייצגת של האופרטור {% equation %}A{% endequation %} היא בעצמה {% equation %}A{% endequation %}, ולכן זה שאנחנו כבר יודעים ש-{% equation %}A^{*}=A{% endequation %} מראה שהאופרטור צמוד לעצמו, ולכן {% equation %}\lambda{% endequation %} הוא אכן ערך עצמי ממשי. עכשיו ממשיכים כמו קודם - פותרים את מערכת המשוואות {% equation %}\left(\lambda I-A\right)x=0{% endequation %}, אבל שימו לב שפותרים אותה <strong>מעל הממשיים</strong> כדי לקבל פתרון ממשי; הפתרון הזה נותן לנו וקטור {% equation %}v\in V{% endequation %} כך ש-{% equation %}T\left(v\right)=\lambda v{% endequation %} וסיימנו ({% equation %}v{% endequation %} עצמו מתקבל מצירוף לינארי של אברי הבסיס {% equation %}B{% endequation %} שבחרנו בהתחלה; הפתרון של מערכת המשוואות אומר לנו מה <strong>המקדמים</strong> של אברי הבסיס הללו בצירוף הלינארי שנותן את {% equation %}v{% endequation %}).

סיימנו את השלב הראשון במה שרצינו לעשות - הראינו שלאופרטור צמוד לעצמו יש תמיד וקטור עצמי. עכשיו מגיע שלב האינדוקציה.

אם כן, יש לנו מרחב מכפלה פנימית {% equation %}V{% endequation %} ממימד {% equation %}n{% endequation %} וטרנספורמציה {% equation %}T{% endequation %} עליו. אנחנו מוצאים וקטור {% equation %}v\in V{% endequation %} כך ש-{% equation %}T\left(v\right)=\lambda v{% endequation %}. שימו לב שאנחנו רוצים לבנות בסיס אורתונורמלי ולכן {% equation %}v{% endequation %} צריך לקיים {% equation %}\|v\|=1{% endequation %}, אבל אם הוא לא מקיים את זה פשוט נחליף אותו ב-{% equation %}\frac{v}{\|v\|}{% endequation %} שהוא גם וקטור עצמי, אז אפשר להניח בלי הגבלת הכלליות ש-{% equation %}v{% endequation %} הוא מנורמה 1. עכשיו אנחנו מגדירים תת-מרחב {% equation %}W=\text{span}\left\{ v\right\} {% endequation %}, ורוצים לפרק את {% equation %}V{% endequation %} אל {% equation %}W{% endequation %} ו"מה שנשאר", כלומר למצוא מרחב אחר, {% equation %}W^{\prime}{% endequation %} כך ש-{% equation %}V=W\oplus W^{\prime}{% endequation %}. למצוא סתם {% equation %}W^{\prime}{% endequation %} אקראי כזה, זה קל: <strong>משלימים לבסיס</strong> את הבסיס של {% equation %}W{% endequation %}, ואז אברי הבסיס הנוספים שמצאנו הם בסיס ל-{% equation %}W^{\prime}{% endequation %}. אבל אנחנו לא רוצים סתם {% equation %}W^{\prime}{% endequation %} אקראי אלא אחד שיהיה מועיל ככל הניתן. בפרט, אנחנו במרחב מכפלה פנימית אז שווה לנצל את המכפלה הפנימית הזו כדי להבטיח של-{% equation %}W^{\prime}{% endequation %} יש מבנה נחמד, ולכן ניקח את {% equation %}W^{\prime}{% endequation %} כך שכל הוקטורים בו <strong>אורתוגונליים</strong> לאלו של {% equation %}W{% endequation %}, מה שנקרא <strong>המשלים האורתוגונלי</strong> {% equation %}W^{\perp}=\left\{ v\in V\ |\ \forall w\in W:\left\langle v,w\right\rangle =0\right\} {% endequation %} של {% equation %}W{% endequation %}. לא קשה להראות שאכן {% equation %}V=W\oplus W^{\perp}{% endequation %} (הראיתי את זה <a href="https://gadial.net/2012/03/01/inner_product_spaces_geometry/">כאן</a>). השאלה היא - למה במקרה הנוכחי זה טוב לנו?

כדי שנוכל להמשיך באינדוקציה, אנחנו צריכים להצטמצם אל {% equation %}W^{\prime}{% endequation %}. בשביל זה צריך שגם {% equation %}T{% endequation %} עצמה תהיה ניתנת לצמצום אליו, וזה לא תמיד קורה: ייתכן שלהפעיל את {% equation %}T{% endequation %} על אברים של {% equation %}W^{\prime}{% endequation %} יוציא אותנו מ-{% equation %}W^{\prime}{% endequation %}. אבל עבור {% equation %}W^{\perp}{% endequation %} ובזכות זה ש-{% equation %}T{% endequation %} היא צמודה לעצמה, זה דווקא כן יהיה אפשרי: פורמלית, לכל {% equation %}v\in W^{\perp}{% endequation %} יתקיים {% equation %}T\left(v\right)\in W^{\perp}{% endequation %}, מה שמסומן לפעמים בתור {% equation %}T\left(W^{\perp}\right)\subseteq W^{\perp}{% endequation %} ומתארים כ"{% equation %}W^{\perp}{% endequation %} הוא {% equation %}T{% endequation %}-אינוריאנטי".

הנה הרעיון: אנחנו מניחים ש-{% equation %}u\in W^{\perp}{% endequation %} ורוצים להראות ש-{% equation %}T\left(u\right)\in W^{\perp}{% endequation %}, כלומר שלכל {% equation %}w\in W{% endequation %} מתקיים {% equation %}\left\langle w,T\left(u\right)\right\rangle =0{% endequation %}, אבל מכיוון ש-{% equation %}T{% endequation %} צמודה לעצמה, {% equation %}\left\langle w,T\left(u\right)\right\rangle =\left\langle T\left(w\right),u\right\rangle {% endequation %}. עכשיו, {% equation %}W{% endequation %} הוא לא סתם תת-מרחב אקראי, הוא בעצמו נפרש על ידי וקטור עצמי של {% equation %}T{% endequation %} ולכן הוא בעצמו {% equation %}T{% endequation %}-אינוריאנטי, כך ש-{% equation %}T\left(w\right)\in w{% endequation %} ולכן {% equation %}\left\langle T\left(w\right),u\right\rangle =0{% endequation %} כי התחלנו מזה ש-{% equation %}u\in W^{\perp}{% endequation %}. זה מסיים את הנימוק הזה.

עכשיו, מכיוון ש-{% equation %}W^{\perp}{% endequation %} הוא {% equation %}T{% endequation %}-אינוריאנטי, אפשר להסתכל על הפונקציה המצומצמת {% equation %}T|_{W^{\perp}}:W^{\perp}\to W^{\perp}{% endequation %}. היא בעצמה אופרטור לינארי צמוד לעצמו, והיא מוגדרת על מרחב ממימד קטן משל {% equation %}W{% endequation %}, אז אפשר להשתמש עליה בהנחת האינדוקציה ומקבלים בסיס אורתונורמלי {% equation %}\left\{ u_{1},\ldots,u_{n-1}\right\} {% endequation %} של וקטורים עצמיים של {% equation %}T|_{W^{\perp}}{% endequation %}, ולכן הם גם וקטורים עצמיים של {% equation %}T{% endequation %}. עכשיו נוסיף להם את {% equation %}v{% endequation %} שמצאנו קודם ונקבל בסיס {% equation %}\left\{ v,u_{1},\ldots,u_{n-1}\right\} {% endequation %} לכל {% equation %}V{% endequation %} (כי {% equation %}V=W\oplus W^{\perp}{% endequation %}) אבל האם זה בסיס <strong>אורתונורמלי</strong>? בשביל זה צריך ש-{% equation %}v{% endequation %} יהיה ניצב לכל ה-{% equation %}u{% endequation %}-ים, אבל... זה בדיוק מה שמובטח לנו מכך שהם איברים של {% equation %}W^{\perp}{% endequation %} בזמן ש-{% equation %}v\in W{% endequation %}. זה מסיים את ההוכחה על לכסון אוניטרי של אופרטורים צמודים לעצמם (במקרה הממשי <strong>וגם</strong> במקרה המרוכב).

<h2>לכסון אוניטרי של דברים נורמליים</h2>

מה שנשאר לנו להוכיח הוא את הטענה הבאה:

<ul> <li>אם {% equation %}V{% endequation %} הוא מרחב מכפלה פנימית מעל {% equation %}\mathbb{C}{% endequation %} ו-{% equation %}T:V\to V{% endequation %} היא נורמלית ({% equation %}T^{*}T=TT^{*}{% endequation %}) אז {% equation %}T{% endequation %} לכסינה אוניטרית.</li>

</ul>

בחלק הקודם שטיפל באופרטורים צמודים לעצמם ראינו שמעל {% equation %}\mathbb{C}{% endequation %} <strong>תמיד</strong> יש ל-{% equation %}T{% endequation %} וקטור עצמי ואז המשכנו באינדוקציה. למה אי אפשר לעשות את זה גם כאן? ובכן <strong>אפשר</strong> לעשות את זה גם כאן, וזה אפילו יעבוד. בערך. ניתקל במכשול כלשהו אבל הנורמליות תסדר לנו אותו.

קודם הרעיון היה לקחת וקטור עצמי {% equation %}v{% endequation %} מנורמה 1 ולבנות את {% equation %}W=\text{span}\left\{ v\right\} {% endequation %} ואז להמשיך באינדוקציה על {% equation %}W^{\perp}{% endequation %}. זה הסתמך על כך ש-{% equation %}W^{\perp}{% endequation %} היה {% equation %}T{% endequation %}-אינוריאנטי, כלומר {% equation %}T\left(W^{\perp}\right)\subseteq W^{\perp}{% endequation %}. לרוע המזל, זה <strong>לא</strong> מה שקורה באופן כללי, כי ההוכחה של זה דרשה ש-{% equation %}T{% endequation %} יהיה צמוד לעצמו; מה שקורה באופן כללי הוא שיש לנו את השרשרת, עבור {% equation %}u\in W^{\perp}{% endequation %} כלשהו וכל {% equation %}w\in W{% endequation %}, של

{% equation %}0=\left\langle T\left(w\right),u\right\rangle =\left\langle w,T^{*}\left(u\right)\right\rangle {% endequation %}

כלומר, {% equation %}T^{*}\left(u\right)\in W^{\perp}{% endequation %}: מה שנכון באופן כללי הוא ש-{% equation %}W^{\perp}{% endequation %} הוא {% equation %}T^{*}{% endequation %}-אינוריאנטי, פשוט במקרה של אופרטור צמוד לעצמו ניצלנו את זה ש-{% equation %}T=T^{*}{% endequation %}. אבל אפשר להתחכם! במקום למצוא וקטור עצמי ל-{% equation %}T{% endequation %}, אני אמצא וקטור עצמי {% equation %}v{% endequation %} עבור {% equation %}T^{*}{% endequation %}, אבנה את {% equation %}W=\text{span}\left\{ v\right\} {% endequation %}, ואז אקבל ש-{% equation %}W^{\perp}{% endequation %} הוא {% equation %}\left(T^{*}\right)^{*}{% endequation %}-אינוריאנטי, כלומר {% equation %}T{% endequation %}-אינוריאנטי, ולכן אפשר לצמצם את {% equation %}T{% endequation %} אל {% equation %}W^{\perp}{% endequation %} ולהפעיל עליו את הנחת האינדוקציה. אבל איך זה עוזר לי, בעצם, אם בסופו של דבר יש לי ביד וקטור עצמי {% equation %}v{% endequation %} של {% equation %}T^{*}{% endequation %} ולא של {% equation %}T{% endequation %}? ובכן, זה הפאנץ': אם {% equation %}T{% endequation %} <strong>נורמלית</strong> אז כל וקטור עצמי של {% equation %}T^{*}{% endequation %} הוא גם וקטור עצמי של {% equation %}T{% endequation %}. זו התוצאה האחרונה שאני צריך להוכיח כדי לסיים את הכל.

יהיו כמה פרטים טכניים, אבל הרעיון הבסיסי הוא פשוט למדי: אם {% equation %}v{% endequation %} הוא וקטור עצמי של {% equation %}T^{*}{% endequation %} עם ערך עצמי {% equation %}\lambda{% endequation %}, זה אומר ש-{% equation %}T^{*}v=\lambda v{% endequation %}, כלומר ש-{% equation %}\left(T^{*}-\lambda I\right)v=0{% endequation %}. בואו נסמן {% equation %}U=T^{*}-\lambda I{% endequation %}. מכללי ההצמדה של אופרטורים, {% equation %}U^{*}=T-\overline{\lambda}I{% endequation %}. עכשיו, אם אני אוכיח שבאופן כללי, אם {% equation %}U{% endequation %} הוא אופטור <strong>נורמלי</strong> אז לכל {% equation %}v\in V{% endequation %} מתקיים {% equation %}\|U\left(v\right)\|=\|U^{*}\left(v\right)\|{% endequation %}, סיימתי. למה? כי

<ol> <li>אם {% equation %}U\left(v\right)=0{% endequation %} כפי שכבר ראינו, אז {% equation %}\|U^{*}\left(v\right)\|=\|U\left(v\right)\|=\|0\|=0{% endequation %}, ולכן {% equation %}U^{*}\left(v\right)=0{% endequation %} (האיבר היחיד מנורמה 0 הוא 0).</li>


<li>אם {% equation %}U^{*}\left(v\right)=0{% endequation %} אז מכך ש-{% equation %}U^{*}=T-\overline{\lambda}I{% endequation %} נקבל {% equation %}T\left(v\right)=\overline{\lambda}v{% endequation %}, כלומר {% equation %}v{% endequation %} הוא גם וקטור עצמי של {% equation %}T{% endequation %}, פשוט לא עבור אותו ערך עצמי אלא עבור ההצמדה שלו.</li>


<li>מכיוון ש-{% equation %}T{% endequation %} הוא אופרטור נורמלי גם {% equation %}U{% endequation %} כזה, כמו שחישוב ישיר יראה.</li>

</ol>

בואו נראה במפורש את ה"חישוב ישיר" של 3 רק כדי שלא יהיה לנו ספק, למרות שזה די ברור גם ככה:

{% equation %}U^{*}U=\left(T-\overline{\lambda}I\right)\left(T^{*}-\lambda I\right)=TT^{*}-\overline{\lambda}T^{*}-\lambda T+\overline{\lambda}\lambda I{% endequation %}

{% equation %}=T^{*}T-\lambda T-\overline{\lambda}T^{*}+\overline{\lambda}\lambda I=\left(T^{*}-\lambda I\right)\left(T-\overline{\lambda}I\right){% endequation %}

אני אוהב את הגישה הזו להוכחה, כי ככה רואים בדיוק איפה תכונת ה"נורמליות" באה לידי ביטוי ובזכותה הכל עובד - כל ההוכחות פה סובבות סביב הדואליות בין {% equation %}T{% endequation %} ו-{% equation %}T^{*}{% endequation %} וחיפוש אחרי מקום כלשהו שבו "המראה נשברת" במובן זה ששני האופרטורים הללו הם לא סתם שיקוף אחד של השני אלא אותו דבר בדיוק.

אוקיי, אז בואו נשבור את המראה. צריך להוכיח ש-{% equation %}\|U\left(v\right)\|=\|U^{*}\left(v\right)\|{% endequation %} לכל {% equation %}v\in V{% endequation %} ואופרטור נורמלי {% equation %}U{% endequation %}. אין כאן יותר לכסונים ועניינים, פשוט חישוב ישיר של נורמות:

{% equation %}\|U\left(v\right)\|^{2}=\left\langle U\left(v\right),U\left(v\right)\right\rangle =\left\langle v,U^{*}U\left(v\right)\right\rangle =\left\langle v,UU^{*}\left(v\right)\right\rangle {% endequation %}

{% equation %}=\left\langle U^{*}\left(v\right),U^{*}\left(v\right)\right\rangle =\|U^{*}\left(v\right)\|^{2}{% endequation %}

ומכיוון שנורמות הן אי-שליליות, אפשר להוציא שורש משני האגפים ולקבל {% equation %}\|U\left(v\right)\|=\|U^{*}\left(v\right)\|{% endequation %} כפי שרצינו, מה שמסיים את ההוכחה.

<h2>לאן הולכים מכאן?</h2>

יש תוצאה מיידית אחת ממה שראינו שאני רוצה להציג כאן לפני שאסיים: <strong>המשפט הספקטרלי</strong>. הרעיון הוא הוא שאם {% equation %}T{% endequation %} הוא אופרטור נורמלי מעל {% equation %}\mathbb{C}{% endequation %} או צמוד לעצמו מעל {% equation %}\mathbb{R}{% endequation %} עם ערכים עצמיים {% equation %}\lambda_{1},\ldots,\lambda_{n}{% endequation %}, אז אפשר לכתוב את {% equation %}T{% endequation %} בתור צירוף לינארי שהמקדמים שלו הם הערכים העצמיים הללו:

{% equation %}T=\lambda_{1}E_{1}+\ldots+\lambda_{n}E_{n}{% endequation %}

כאשר ה-{% equation %}E_{1},\ldots,E_{n}{% endequation %} הן <strong>ההטלות האורתונוגליות</strong> על המרחבים העצמיים {% equation %}W_{1},\ldots,W_{n}{% endequation %}.

מה זו הטלה אורתוגונלית? ובכן, נכון שדיברנו קודם על מרחב {% equation %}V{% endequation %} שמתחלק אל {% equation %}W\oplus W^{\perp}{% endequation %}? זה אומר שכל וקטור {% equation %}v{% endequation %} אפשר לכתוב בתור {% equation %}v=w+u{% endequation %} כך ש-{% equation %}w\in W,u\in W^{\perp}{% endequation %}. הטלה אורתוגונלית על {% equation %}W{% endequation %} היא האופרטור שלוקח את {% equation %}v{% endequation %} ומחזיר את {% equation %}w{% endequation %}, כלומר את הרכיב שלו ששייך ל-{% equation %}W{% endequation %} בפירוק של {% equation %}v{% endequation %} ל"משהו מ-{% equation %}W{% endequation %} ועוד משהו שמאונך ל-{% equation %}W{% endequation %}". אנחנו רגילים לזה מחיי היום יום המתמטיים: אם יש לנו את הקואורדינטה {% equation %}\left(x,y\right){% endequation %} ואנחנו שולפים ממנה את {% equation %}x{% endequation %}, ביצענו הטלה אורתוגונלית; עצם השימוש שלנו ב-{% equation %}\left(x,y\right){% endequation %} כדי לתאר וקטורים ב-{% equation %}\mathbb{R}^{2}{% endequation %} מראה כמה טבעי לנו לחשוב כל הזמן במונחים של מרחבים אורתונורמליים ("ציר {% equation %}x{% endequation %} וציר {% equation %}y{% endequation %}").

בשביל הוכחת המשפט הספקטרלי, אני רוצה קודם כל להראות שכל שני מרחבים עצמיים שונים {% equation %}W_{i},W_{j}{% endequation %} הם אורתוגונליים זה לזה. אז אני אקח {% equation %}v\in W_{i}{% endequation %} ו-{% equation %}u\in W_{j}{% endequation %} כך ש-{% equation %}T\left(v\right)=\lambda v{% endequation %} ו-{% equation %}T\left(u\right)=\rho u{% endequation %} ו-{% equation %}\lambda\ne\rho{% endequation %} וכרגיל אעשה איזה להטוט עם המכפלה הפנימית:

{% equation %}\lambda\left\langle v,u\right\rangle =\left\langle \lambda v,u\right\rangle =\left\langle T\left(v\right),u\right\rangle ={% endequation %}

{% equation %}=\left\langle v,T^{*}\left(u\right)\right\rangle =\left\langle v,\overline{\rho}u\right\rangle =\rho\left\langle v,u\right\rangle {% endequation %}

כאן השתמשתי בכך ש-{% equation %}T{% endequation %} נורמלי ולכן {% equation %}u{% endequation %} הוא וקטור עצמי של {% equation %}T^{*}{% endequation %}, פשוט עם הערך העצמי {% equation %}\overline{\rho}{% endequation %}, כפי שראינו קודם.

קיבלתי ש-{% equation %}\left(\lambda-\rho\right)\left\langle v,u\right\rangle =0{% endequation %} ומכיוון ש-{% equation %}\lambda\ne\rho{% endequation %} המסקנה היא {% equation %}\left\langle v,u\right\rangle =0{% endequation %}, כפי שרציתי. עכשיו, מכך שיש לנו לכסון אוניטרי של {% equation %}T{% endequation %} אנחנו מקבלים שהמרחבים העצמיים של {% equation %}T{% endequation %} פורשים את כל {% equation %}V{% endequation %}, כלומר {% equation %}V=W_{1}+\ldots+W_{n}{% endequation %}. כדי לראות שזה סכום ישר, אפשר להסתכל על צירוף לינארי {% equation %}w_{1}+\ldots+w_{n}=0{% endequation %} כך ש-{% equation %}w_{i}\in W_{i}{% endequation %}, לכפול אותו ב-{% equation %}w_{i}{% endequation %} עבור {% equation %}1\le i\le n{% endequation %} ולקבל

{% equation %}0=\left\langle 0,w_{i}\right\rangle =\left\langle \sum_{k=1}^{n}w_{k},w_{i}\right\rangle =\sum_{k=1}^{n}\left\langle w_{k},w_{i}\right\rangle =\|w_{i}\|^{2}{% endequation %}

וזה כי אנחנו יודעים מהלכסון האוניטרי שוקטורים עצמיים שמתאימים לערכים עצמיים שונים יהיו אורתוגונליים. המסקנה היא ש-{% equation %}w_{i}=0{% endequation %} לכל אחד מאברי הסכום, כלומר הצירוף הלינארי היחיד שנותן את 0 הוא 0, וזה שקול לכך ש-{% equation %}V=W_{1}\oplus\ldots\oplus W_{n}{% endequation %}. זה אומר שכל {% equation %}v{% endequation %} ניתן להצגה יחידה בתור {% equation %}v=w_{1}+\ldots+w_{n}{% endequation %} ואם נסמן ב-{% equation %}E_{i}{% endequation %} את ההטלה האורתוגונלית מ-{% equation %}V{% endequation %} על {% equation %}W_{i}{% endequation %}, אז מה שהיא עושה הוא {% equation %}E_{i}\left(v\right)=w_{i}{% endequation %}. 

בפרט, שימו לב ש-{% equation %}E_{1}+\ldots+E_{n}=I{% endequation %}, כי פשוט תפעילו את אגף שמאל על {% equation %}v{% endequation %} ותראו מה תקבלו; ובאופן דומה:

{% equation %}T\left(v\right)=T\left(\sum_{i=1}^{n}w_{i}\right)=\sum_{i=1}^{n}T\left(w_{i}\right)=\sum_{i=1}^{n}\lambda_{i}w_{i}=\sum_{i=1}^{n}\lambda_{i}E_{i}\left(v\right){% endequation %}

מה שנותן לנו את {% equation %}T=\lambda_{1}E_{1}+\ldots+\lambda_{n}E_{n}{% endequation %} המובטח.

הדבר הבא שמעניין לטעמי לדבר עליו אחרי שרואים לכסון אוניטרי הוא ההכללה שלו, למשהו שעובד במרחב מכפלה פנימית סוף ממדי עבור <strong>כל</strong> מטריצה, כולל מטריצות לא ריבועיות בכלל: פירוק לערכים סינגולריים (Singular Value Decomposition, ובקיצור SVD). כאן הרעיון הוא בגדול להציג מטריצה {% equation %}A{% endequation %} על ידי <strong>שתי</strong> מטריצות אוניטריות ומטריצה אלכסונית, {% equation %}A=U\Sigma V^{*}{% endequation %}, אבל מה המטריצות מייצגות? מה הולך באלכסון של {% equation %}\Sigma{% endequation %}? מה זה "ערכים סינגולריים"? לזה ראוי להקדיש פוסט משל עצמו, וזה מה שאני מתכנן לעשות בפוסט הבא. אני רק מקווה ש"הפוסט הבא" כאן לא יתגלה גם בתור "נחכה 12 שנים ואז ניזכר לכתוב אותו". 