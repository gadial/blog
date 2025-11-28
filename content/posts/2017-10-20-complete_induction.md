---
id: 3513
title: "אינדוקציה שלמה ואינדוקציה רגילה"
date: 2017-10-20 17:16:42
layout: post
categories: 
  - כללי
  - לוגיקה
tags: 
  - אינדוקציה מתמטית
  - אינדוקציה שלמה
---
פנו אלי בשאלה פשוטה: איך מוכיחים את עקרון האינדוקציה השלמה מעקרון האינדוקציה הרגיל? ובכן, בואו נסביר על מה מדובר בכלל, ואיך מוכיחים.

אינדוקציה "רגילה" היא דרך מקובלת במתמטיקה להסיק טענה כללית: מתחילים ממקרים פרטיים ספציפיים שבהם קל להראות את הטענה באופן מפורש, ואז מציגים "תבנית הוכחה" שהיא מהצורה "אם המקרה הפשוט הזה נכון, אז גם המקרה היותר מסובך הזה נכון". הרעיון הוא שלכל מקרה שנרצה להוכיח, נוכל איכשהו להתחיל ממקרה פרטי שעבורו כבר הוכחנו את הטענה, ואז להסיק ממנו, באמצעות תבנית ההוכחה שלנו, מקרים יותר ויותר מסובכים עד שנגיע אל המקרה הספציפי שאנחנו רוצים להוכיח.

את התיאור המאוד כללי ומנופנף ידיים הזה לרוב דוחסים לתוך המסגרת המאוד פשוטה של המספרים הטבעיים - המספרים {% equation %}1,2,3,4,\dots{% endequation %} (נעזוב את 0 להפעם). הרעיון הוא שיש לנו סדרה של טענות, כשכל טענה מתאימה למספר טבעי אחר. למשל, השווין {% equation %}1+2+3+\dots+n=\frac{n\left(n+1\right)}{2}{% endequation %} הוא בעצם דרך כללית לתאר את הסדרה הבאה של טענות:

טענה מס' 1: {% equation %}1=\frac{1\left(1+1\right)}{2}{% endequation %}

טענה מס' 2: {% equation %}1+2=\frac{2\left(2+1\right)}{2}{% endequation %}

טענה מס' 3: {% equation %}1+2+3=\frac{3\left(3+1\right)}{2}{% endequation %}

וכך זה נמשך ונמשך.

אינדוקציה "רגילה" אומרת את הדבר הבא: נניח שאנחנו יודעים להוכיח את הטענה במפורש עבור {% equation %}n=1{% endequation %} (<strong>הבסיס</strong>) ונניח גם ש<strong>אם</strong> נתון לנו שהטענה נכונה עבור {% equation %}n{% endequation %} כלשהו אז אנחנו יודעים להוכיח שהטענה נכונה עבור {% equation %}n+1{% endequation %} (<strong>הצעד</strong>) אז הטענה נכונה לכל {% equation %}n{% endequation %}. האינטואיציה היא שכדי להוכיח את טענה 3, למשל, אנחנו מבצעים שרשרת של טענות מהצורה "אוקיי, קודם כל טענה 1 נכונה כי הנה הוכחה מפורשת. עכשיו, אני יודע להוכיח ש<strong>אם</strong> טענה 1 נכונה אז גם טענה 2 נכונה, וכבר ראיתי שטענה 1 נכונה אז המסקנה היא שטענה 2 נכונה. עכשיו, אני יודע להוכיח ש<strong>אם </strong>טענה 2 נכונה אז גם טענה 3 נכונה, וכבר ראינו ש-2 נכונה ולכן גם 3 נכונה". עבור טענה 1,000,000 אותו עיקרון בדיוק יעבוד, אם כי השרשרת שתיווצר תהיה מפלצתית באורכה (אבל האורך הזה יהיה סופי, שזו הנקודה החשובה פה כי הוכחות אמורות להיות תמיד סופיות).

אינדוקציה "שלמה" אומרת את הדבר הבא: נניח ש<strong>אם </strong>נתון לנו שהטענה נכונה <strong>לכל</strong> מספר טבעי מ-1 ועד {% equation %}n{% endequation %}, אז אנחנו יודעים להוכיח את הטענה עבור {% equation %}n+1{% endequation %}, אז מכאן נובע שהטענה נכונה לכל {% equation %}n{% endequation %}. כאן אין הבדלה בין הבסיס ובין הצעד, כי הבסיס הוא הסיטואציה שבה {% equation %}n=0{% endequation %}, ואז ה"צעד" אומר את הדבר הבא: אנחנו יודעים להוכיח שהטענה נכונה עבור 1 <strong>אם</strong> נתון לנו שהיא נכונה לכל מספר טבעי שגדול או שווה ל-1 אבל קטן או שווה ל-0, כלומר במקרה הזה לא נתון לנו כלום, וזו בדיוק הסיטואציה של להוכיח את המקרה {% equation %}n=1{% endequation %} בלי כלום.

מה ההבדל בין אינדוקציה רגילה ושלמה? באינדוקציה שלמה <strong>יש יותר על מה להתבסס</strong> כשבאים להוכיח שהטענה נכונה עבור {% equation %}n+1{% endequation %}. באינדוקציה רגילה כל מה שיש לנו הוא את נכונות הטענה עבור {% equation %}n{% endequation %}, וזהו; אבל אולי המקרה עבור {% equation %}n{% endequation %} לא רלוונטי עבור {% equation %}n+1{% endequation %} ודווקא קל להוכיח את המקרה {% equation %}n+1{% endequation %} אם נתונה לנו הטענה עבור {% equation %}n-1{% endequation %}? לכן אינדוקציה שלמה באה להגיד לנו - קחו איזה מקרה שתרצו מבין אלו ש"כבר עברתם". אם נחשוב על זה לרגע, כשאני מוכיח את המקרה {% equation %}n=5{% endequation %} באינדוקציה <strong>רגילה</strong>, מה שאני עושה הוא קודם כל לייצר הוכחות עבור המקרים {% equation %}1,2,3,4{% endequation %} ואז להשתמש רק במקרה 4 כדי להוכיח את 5. אין סיבה עקרוני למה לא להשתמש גם ב"תוצרי הלוואי" שהוכחתי בדרך - 1,2,3.

אם לסכם - אינדוקציה שלמה נראית <strong>חזקה יותר</strong> כי היא נותנת לנו בצעד האינדוקציה יותר מידע שאפשר להתבסס עליו, אבל בפועל זה לא מידע שצץ משום מקום - גם באינדוקציה רגילה הוא נוצר, והאינדוקציה הרגילה פשוט "שוכחת ממנו". תחשבו על האופן שבו אנחנו לפעמים קוראים ערכים בויקיפדיה: אנחנו נכנסים לערך כלשהו, באמצע הקריאה לוחצים על לינק ומתחילים לקרוא על ערך אחר, ואז על ערך אחר וכן הלאה; כשאנחנו עוברים ערך אנחנו יכולים או סתם ללחוץ על הלינק והדפדפן יעבור לערך החדש, או שאנחנו יכולים לפתוח את הלינק בטאב חדש, תוך שאנחנו שומרים את הטאבים שכוללים את כל הערכים שבהם היינו עד כה. זו המחשה להבדל בין שתי הגישות.

אז למה אנחנו כאן? בשביל הפורמליזם. השאלה המעניינת היא זו: נניח שאנחנו יודעים שהמספרים הטבעיים מקיימים את תכונת האינדוקציה הרגילה; איך אפשר להסיק מכך שהם מקיימים את תכונת האינדוקציה השלמה? איך עושים את זה פורמלית? ולמה בעצם זו בעיה?

כדי לפשט טיפה את הדיון מבלי לפגוע במהות שלו, בואו נציג ניסוח קצת יותר נקי של מהי אינדוקציה. במקום לדבר על "תכונות" נדבר על קבוצות. אינדוקציה רגילה אומרת את הדבר הבא: תהא {% equation %}S{% endequation %} קבוצה כלשהי של מספרים טבעיים. אם {% equation %}1\in S{% endequation %} וגם ידוע שלכל {% equation %}n{% endequation %} טבעי, אם {% equation %}n\in S{% endequation %} אז {% equation %}n+1\in S{% endequation %}, אז המסקנה היא ש-{% equation %}S=\mathbb{N}{% endequation %}, דהיינו {% equation %}S{% endequation %} כוללת את כל הטבעיים. בואו ננסח את זה בצורה יותר פורמלית, כדי למנוע ככל הניתן כפלי משמעות שהשפה מכניסה:

{% equation %}\forall S\left[\left(1\in S\wedge\left(\forall n\left(n\in S\to n+1\in S\right)\right)\right)\to S=\mathbb{N}\right]{% endequation %}

הניסוח הזה הוא עדיין כתיבה בנפנוף ידיים כלשהו - זה לא פסוק שמתאים בדיוק לכל כללי הלוגיקה הפורמלית, אבל זה מספיק טוב לצריכנו, שהם לתאר פורמלית את מה שקורה פה. עכשיו אנסח אינדוקציה שלמה בצורה דומה:

{% equation %}\forall S\left[\left(\forall n\left(\forall k\left(k&lt;n\to k\in S\right)\to n\in S\right)\right)\to S=\mathbb{N}\right]{% endequation %}

בואו ננסה להבין איך צריכה להיראות הוכחה פורמלית יחסית לדברים הללו. ראשית, ה-{% equation %}\forall S{% endequation %} הזה אומר שאני צריך לקחת {% equation %}S{% endequation %} <strong>כלשהי</strong> ולהוכיח את הטענה בסוגריים עבור אותה {% equation %}S{% endequation %}. כלומר, מה שנשאר להוכיח הוא כעת

{% equation %}\left(\forall n\left(\forall k\left(k&lt;n\to k\in S\right)\to n\in S\right)\right)\to S=\mathbb{N}{% endequation %}

זו טענה מהמבנה הכללי {% equation %}A\to B{% endequation %}. טענות כאלו הן נכונות תמיד, למעט במקרה שבו {% equation %}A{% endequation %} הוא "אמת" ואילו <strong>{% equation %}B{% endequation %} </strong>הוא "שקר". כלומר, היעד שלנו הוא להראות שהמקרה הזה לא מתאפשר. מכיוון שבמקרה הזה {% equation %}A{% endequation %} הוא "אמת" אני יכול להוסיף את {% equation %}A{% endequation %} להנחות שלי, ומכיוון שאני רוצה להראות שגם {% equation %}B{% endequation %} הוא אמת, אני רוצה להוכיח את {% equation %}B{% endequation %}. במילים אחרות, אם אני מתחזק לעצמי שתי רשימות - רשימה של "ההנחות שלי" ורשימה של "הדברים שעלי להוכיח", ורשימת "הדברים שעלי להוכיח" כללה את {% equation %}A\to B{% endequation %}, אז אני מוציא את {% equation %}A\to B{% endequation %} מהרשימה הזו, מוסיף לה את {% equation %}B{% endequation %} ומוסיף את {% equation %}A{% endequation %} לרשימת ההנחות שלי.

על כן, ה"צריך להוכיח" שלי כולל דבר יחיד: {% equation %}S=\mathbb{N}{% endequation %}. ההנחות שלי כוללות את הרישא של נוסחת האינדוקציה השלמה, ואת <strong>כל</strong> נוסחת האינדוקציה הרגילה. כלומר, יש לי שתי הנחות:
<ol>
	<li>{% equation %}\forall n\left(\forall k\left(k&lt;n\to k\in S\right)\to n\in S\right){% endequation %}</li>
	<li>{% equation %}\left(1\in S\wedge\left(\forall n\left(n\in S\to n+1\in S\right)\right)\right)\to S=\mathbb{N}{% endequation %}</li>
</ol>
את הנחה מס' 2 אפשר לנצל בצורה הבאה: הסיפא שלה היא בדיוק מה שאני צריך להוכיח, ולכן אם אוכיח את הרישא שלה, סיימתי. זה אומר שאני יכול <strong>להחליף</strong> את הצריך להוכיח המקורי שלי בנוסחה הבאה:

{% equation %}1\in S\wedge\left(\forall n\left(n\in S\to n+1\in S\right)\right){% endequation %}

אלו בעצם שני "צריך להוכיח" שונים שכתובים יחד. רשימת ה"צריך להוכיח" שלי, אם כן, היא כעת:
<ol>
	<li>{% equation %}1\in S{% endequation %}</li>
	<li>{% equation %}\forall n\left(n\in S\to n+1\in S\right){% endequation %}</li>
</ol>
וההנחה שבאמצעותה אני אמור להוכיח את שני אלו היא זו: {% equation %}\forall n\left(\forall k\left(k&lt;n\to k\in S\right)\to n\in S\right){% endequation %}. בואו נראה איך זה מוכיח את 1: ההנחה מתקיימת לכל {% equation %}n{% endequation %}, ולכן בפרט עבור הבחירה {% equation %}n=1{% endequation %}. כשמציבים את הבחירה הזו בהנחה, מקבלים

{% equation %}\left(\forall k\left(k&lt;1\to k\in S\right)\to1\in S\right){% endequation %}. כמו קודם, אנחנו יכולים להחליף את ה"צריך להוכיח" הנוכחי שלנו, {% equation %}1\in S{% endequation %}, ברישא של הפסוק הזה, {% equation %}\forall k\left(k&lt;1\to k\in S\right){% endequation %}. אצלנו הטבעיים לא כוללים את 0, ולכן {% equation %}k&lt;1{% endequation %} הוא משהו שלא מתקיים לאף טבעי. לכן הנוסחה {% equation %}\forall k\left(k&lt;1\to k\in S\right){% endequation %} היא נכונה תמיד (אם הרישא היא "שקר" לא אכפת לנו אם הסיפא היא אמת או שקר). זה מסיים את זה.

עד עכשיו הכל עבד כל כך חלק, אז איפה הבעיה בעצם? בדיוק בשלב הבא: נשאר לי להוכיח ש-

{% equation %}\forall n\left(n\in S\to n+1\in S\right){% endequation %}

כלומר, עבור {% equation %}a{% endequation %} שרירותי כלשהו, אנחנו רוצים להוכיח ש-{% equation %}a\in S\to a+1\in S{% endequation %} (בכוונה החלפתי את האות). במילים אחרות, אנחנו רוצים להוכיח את {% equation %}a+1\in S{% endequation %} עם ההנחה {% equation %}a\in S{% endequation %} והנחה נוספת: ההנחה החזקה-לכאורה של אינדוקציה שלמה, שאומרת ש- {% equation %}\forall n\left(\forall k\left(k&lt;n\to k\in S\right)\to n\in S\right){% endequation %}. אם אני אציב {% equation %}n=a+1{% endequation %}, הסיפא של ההנחה שלי תהיה בדיוק מה שאני חותר אליו, ויישאר לי רק להראות את {% equation %}\forall k\left(k&lt;a+1\to k\in S\right){% endequation %}. וכאן אני נתקע.

למה אני נתקע? כי לא נתון לי ש-{% equation %}k\in S{% endequation %} <strong>לכל</strong> {% equation %}k&lt;a+1{% endequation %}; זה נתון רק עבור {% equation %}k{% endequation %} ספציפי - {% equation %}k=a{% endequation %}. ההנחה הרחבה של האינדוקציה השלמה היא <strong>חסרון</strong> במקרה הנוכחי, כי בניגוד לסיטואציות הרגילות שבהן אני <strong>משתמש</strong> באינדוקציה שלמה, ואז זה מקל על החיים, כאן אני מנסה להוכיח <strong>את עקרון האינדוקציה השלמה עצמו</strong>, ולצורך כך אני צריך לקושש <strong>יותר</strong> נתונים מאשר בדרך כלל. לכאורה נתקעתי.

הפתרון הוא פתרון סטנדרטי כאשר משתמשים באינדוקציה ונתקעים - <strong>לחזק את הנחת האינדוקציה</strong>. כשמוכיחים את צעד האינדוקציה מוכיחים {% equation %}n\in S\to n+1\in S{% endequation %}. כאן אנחנו נעזרים ב<strong>הנחה</strong> {% equation %}n\in S{% endequation %} כדי להוכיח את ה<strong>צעד</strong> {% equation %}n+1\in S{% endequation %}. אם ההנחה {% equation %}n\in S{% endequation %} לא מספיק טובה לנו, אנחנו מחליפים את {% equation %}S{% endequation %} כולה ב-{% equation %}S^{\prime}{% endequation %} שהיא <strong>חיזוק</strong> של {% equation %}S{% endequation %} - כלומר, היא תכונה שכל מי שמקיים אותה מקיים גם את {% equation %}S{% endequation %}, אבל כוללת יותר אינפורמציה שאפשר לנצל. בצורה הזו אנחנו מקבלים את ההנחה החזקה יותר {% equation %}n\in S^{\prime}{% endequation %} ואם בחרנו את {% equation %}S^{\prime}{% endequation %} בחוכמה, נוכל להוכיח את הצעד החזק יותר (ולכן הקשה יותר להוכחה) {% equation %}n+1\in S^{\prime}{% endequation %} יותר בקלות.

במקרה שלנו החיזוק הוא די ברור: {% equation %}S^{\prime}=\left\{ n\in S\ |\ \forall k&lt;n\left(k\in S\right)\right\} {% endequation %}. כלומר, התכונה שלנו עכשיו היא "אני מקיים את {% equation %}S{% endequation %} וכך גם כל מי שקטן ממני". בבירור {% equation %}S^{\prime}\subseteq S{% endequation %} ולכן אם אוכיח {% equation %}S^{\prime}=\mathbb{N}{% endequation %} ינבע מכך {% equation %}S=\mathbb{N}{% endequation %}. בשביל להוכיח ש-ּ{% equation %}S^{\prime}=\mathbb{N}{% endequation %} צריך להוכיח את שתי הטענות שהצגתי קודם:
<ol>
	<li>{% equation %}1\in S^{\prime}{% endequation %}</li>
	<li>{% equation %}\forall n\left(n\in S^{\prime}\to n+1\in S^{\prime}\right){% endequation %}</li>
</ol>
מבין שתיהן, הטענה הראשונה כבר טופלה - כבר ראינו ש-{% equation %}1\in S{% endequation %} ומכיוון שלא קיים {% equation %}k&lt;1{% endequation %} אז השייכות {% equation %}1\in S^{\prime}{% endequation %} נובעת מיידית. נשאר רק להוכיח את צעד האינדוקציה ה"מחוזק", כלומר ש-{% equation %}a\in S^{\prime}\to a+1\in S^{\prime}{% endequation %}. כעת, אם {% equation %}a\in S^{\prime}{% endequation %} אז מהגדרת {% equation %}S^{\prime}{% endequation %} נקבל ש-{% equation %}k\in S{% endequation %} לכל {% equation %}k&lt;a+1{% endequation %}. זה אומר שכדי להראות ש-{% equation %}a+1\in S^{\prime}{% endequation %} צריך אך ורק להראות ש-{% equation %}a+1\in S{% endequation %}. עכשיו מצבנו השתפר! אנחנו צריכים להוכיח את הטענה

{% equation %}a+1\in S{% endequation %}

שגם קודם הסתבכנו איתה, אבל עכשיו יש לנו הנחה חזקה יותר:

{% equation %}a\in S^{\prime}{% endequation %}

וההנחה הזו נותנת לנו את מה שהיה חסר לנו קודם: {% equation %}k\in S{% endequation %} לכל {% equation %}k&lt;a+1{% endequation %}. עם ההנחה הזו אפשר להשתמש בהנחה הנוספת שקיבלנו מעקרון האינדוקציה השלמה ולקבל {% equation %}a+1\in S{% endequation %} כפי שרצינו, מה שמסיים את ההוכחה.

לסיכום, אין בעקרון האינדוקציה השלמה שום דבר מתוחכם במיוחד - הוא דוגמא בסיסית לאופן שבו אפשר <strong>לחזק</strong> את עקרון האינדוקציה הרגיל על ידי שינוי התכונה שאותה מוכיחים באינדוקציה. אבל זה אחד מהמקרים הללו שבהם קשה להבין מה בעצם הבעיה עד שלא חופרים בו טכנית לעומק.
