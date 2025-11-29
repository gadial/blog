---
id: 3759
title: "משפטי נקודת השבת של בנך וברואר"
date: 2019-03-23 14:42:33
layout: post
categories: 
  - אנליזה מתמטית
tags: 
  - משפט נקודת השבת של בנך
  - משפט נקודת השבת של ברואר
  - נקודת שבת
social_media_share: true
---
<h2>מבוא</h2>
בואו נתחיל עם סיפור קצרצר בן פסקה אחת של חורחה לואיס בורחס בשם "על הדיוק במדע" שאני מביא פה בתרגום יורם ברונובסקי:
<blockquote>...באימפריה זו הגיעה אמנות כתיבת המפות למידת שלמות כזו, שמפתו של מחוז אחד השתרעה על פני עיר שלמה ואילו מפתה של האימפריה כולה - על פני המחוז כולו. ברבות הימים לא סיפקו עוד מפות ענק אלה את התשובות וועדות כותבי המפות החלו להכין את מפת האימפריה שגודלה כגודל האימפריה עצמה, והיא זהה עמה בכל נקודה ונקודה. הדורות הבאים היו אדוקים פחות במדע כתיבת המפות, הם גרסו שמפה נרחבת זו היא מיותרת והפקידו אותה לאכזריות השמש והחורף. במדבריות המערב שרדו כמה חורבות של המפה, שם שוכנים חיות בר וקבצנים, בארץ כולה לא היו שרידים נוספים של מדע כתיבת הארץ.

(מתוך "מסעות אנשי החיל" לסוארס מיראנדה, ספר רביעי, פרק מ"ה, לרידה, 1658.)</blockquote>
לא, אל תחפשו את "מסעות אנשי החיל" לסוארס מיראנדה, הוא קיים בערך כמו ספר מפורסם אחר של אחד, ס. מורגנשטרן.

איך כל זה קשור למתמטיקה? ובכן, על משמעות כלליות מהסיפור אפשר לדבר בפעם אחרת, הפעם הבאתי אותו כי המוטיבציה שלי לכתיבת הפוסט היא דבר אחר, דומה, שגם כן מערב מפות: ההבחנה שאם ניקח מפה של ארץ כלשהי (לא בהכרח 1:1 כמו המפה של בורחס) ונניח אותה על הקרקע של הארץ שמתוארת בה, אז תהיה נקודה על המפה שנמצאת <strong>בדיוק</strong> מעל הנקודה על הקרקע הפיזית שהנקודה הזו במפה מתארת. תמיד. וגם אם נזיז קצת את המפה - עדיין תהיה. וכן, גם אם ננסה בכוונה להניח את המפה על הקרקע כך שזה לא יקרה, זה יקרה. וגם אם נסובב את המפה - זה יקרה. ומה שנחמד פה כל כך הוא שהתוצאה הזו היא המחשה יפה של <strong>משפט נקודת השבת של בנך</strong>; והמשפט הזה גם מצביע על הדרך שבה אפשר למצוא את הנקודה שבה זה קורה.

משפט נקודת השבת של בנך הוא הדבר העיקרי שאני רוצה להראות בפוסט הזה, ברמת הניסוח המלא וההוכחה. על הדרך אני גם אנצל את ההזדמנות ואסביר כמעט כל מושג שבו אני משתמש, כי המשפט הזה הוא הזדמנות טובה עבורנו לחזור על מושגי הבסיס הללו.

אפשר לחשוב על משפט נקודת השבת של בנך בתור "כמעט מקרה פרטי" של משפט מפורסם עוד יותר, <strong>משפט נקודת השבת של ברואר</strong> (למה רק "כמעט"? אדבר על ההבדלים המדויקים בהמשך). גם למשפט של ברואר יש אילוסטרציות נחמדות: נניח שאתם מערבבים כוס משקה, אז מובטח שתהיה נקודה אחת בכוס שאחרי כל הערבובים חזרה למקום שבו התחילה. או אילוסטרציה אחרת: קחו שני דפים מאותו הגודל, שימו אחד על השני, ואז קמטו את הדף שלמעלה כמה שתרצו - עדיין תהיה נקודה אחת לפחות בדף המקומט שנמצאת בדיוק מעל הנקודה שמתאימה לה בדף שמתחת. על המשפט של ברואר אני אגניב כמה מילים בסוף אבל לא אוכיח אותו הפעם, כי זו לא הוכחה כמעט-מיידית כמו של בנך.
<h2>משפט נקודת השבת של בנך</h2>
מה הרעיון במפה? מפה היא עותק מוקטן של פני השטח במציאות (אלא אם אנחנו בסיפור של בורחס). אם תרצו, אנחנו <strong>מכווצים</strong> את המרחב שלנו אל תת-מרחב ספציפי, במובן זה שה<strong>מרחק</strong> בין נקודות הופך לקטן יותר. משפט נקודת השבת של בנך עוסק בדיוק בסיטואציה הזו - העתקה ממרחב לעצמו שהיא <strong>מכווצת</strong>. זה דורש ממני להגדיר מה הכוונה ב"מרחב" ואיך אני מודד "מרחק" וכדומה, ויש לי תשובות שונות ומשונות לזה בהתאם להיכרות שיש לכם עם מתמטיקה. נתחיל עם הדוגמא הפשוטה: המרחב שלנו הוא פשוט <strong>המישור</strong>, {% equation %}X=\mathbb{R}^{2}{% endequation %}, אוסף הנקודות מהצורה {% equation %}\left(a,b\right){% endequation %} כאשר {% equation %}a,b\in\mathbb{R}{% endequation %}. האופן שבו מודדים מרחק בין שתי נקודות במישור הוא על ידי הנוסחה {% equation %}d\left(\left(a_{1},a_{2}\right),\left(b_{1},b_{2}\right)\right)=\sqrt{\left(a_{1}-b_{1}\right)^{2}+\left(a_{2}-b_{2}\right)^{2}}{% endequation %} (זה בעצם <strong>משפט פיתגורס</strong> בפעולה).

זה נותן לנו מרחב קונקרטי להתייחס אליו, אבל למה לעצור שם? האם המשפט לא יעבוד גם עבור תת-קבוצה של המרחב הזה, נאמר ריבוע היחידה {% equation %}X=\left[0,1\right]\times\left[0,1\right]{% endequation %}? והאם הוא לא יעבוד עבור {% equation %}X=\mathbb{R}^{3}{% endequation %}? ומה אם אנחנו מודדים מרחק בדרך קצת שונה, למשל {% equation %}d\left(\left(a_{1},a_{2}\right),\left(b_{1},b_{2}\right)\right)=\left|a_{1}-b_{1}\right|+\left|a_{2}-b_{2}\right|{% endequation %}? המשפט ימשיך לעבוד בכל המקרים הללו, ולכן כדי לדבר על כולן בבת אחת אנחנו מדברים על מושג שנקרא <strong>מרחב מטרי</strong>. מרחב מטרי {% equation %}\left(X,d\right){% endequation %} כולל קבוצה {% equation %}X{% endequation %} ופונקציית מרחק {% equation %}d:X^{2}\to\mathbb{R}^{\ge0}{% endequation %} כך שלכל {% equation %}a,b,c\in X{% endequation %}:
<ol>
 	<li>{% equation %}d\left(a,b\right)=0{% endequation %} אם ורק אם {% equation %}a=b{% endequation %}</li>
 	<li>{% equation %}d\left(a,b\right)=d\left(b,a\right){% endequation %} (סימטריה)</li>
 	<li>{% equation %}d\left(a,b\right)\le d\left(a,c\right)+d\left(c,b\right){% endequation %} (אי-שוויון המשולש)</li>
</ol>
ההגדרה הפשוטה הזו מאפשרת דיבור אחיד על כל המקרים שציינתי קודם ואינספור מקרים אחרים, וזה ההקשר שבו נכון לתאר את משפט נקודת השבת של בנך; אבל למי שמתקשים עם הדיבור האבסטרקטי על מרחבים מטריים, אפשר לחשוב כל הזמן על המקרה הקונקרטי {% equation %}X=\mathbb{R}^{2}{% endequation %} ו-{% equation %}d\left(\left(a_{1},a_{2}\right),\left(b_{1},b_{2}\right)\right)=\sqrt{\left(a_{1}-b_{1}\right)^{2}+\left(a_{2}-b_{2}\right)^{2}}{% endequation %} שהזכרתי קודם. עובד באותה מידה.

דרישה אחת מהמרחב כדי שהמשפט יעבוד היא שהוא יהיה <strong>שלם</strong>. מרחב מטרי שלם הוא מרחב שבו כל סדרת קושי מתכנסת, אבל אם זה לא אומר לכם שום דבר כרגע זה לא צריך לעצור אתכם - בהמשך נבין בדיוק מה זו סדרת קושי ולמה היא מעניינת אותנו. {% equation %}\mathbb{R}^{2}{% endequation %} הוא מרחב שלם, כך שהמשפט יהיה תקף לגביו. דוגמא למרחב לא שלם היא {% equation %}\mathbb{Q}{% endequation %} - שם המחסור בנקודות כמו {% equation %}\sqrt{2}{% endequation %} ו-{% equation %}\pi{% endequation %} יוצר בעיה של ממש (אפשר לקבל משהו בסגנון "נקודת השבת <strong>צריכה</strong> להיות {% equation %}\sqrt{2}{% endequation %} אבל היי, רגע, מה הולך פה, לאן היא נעלמה?")

עכשיו צריך להכניס לתמונה פונקציה, {% equation %}f:X\to X{% endequation %}. אם רוצים לקשר את זה לדוגמת המפה שאיתה פתחתי, אפשר לחשוב על פונקציה שפועלת כך: בהינתן נקודה בארץ שהמפה מתארת (הארץ הזו היא {% equation %}X{% endequation %}), הפונקציה מאתרת את הנקודה המתאימה על המפה, הולכת אל הנקודה הזו ומחזירה את הנקודה על הקרקע של הארץ "האמיתית" שנוגעת בנקודה הזו במפה. באופן הזה קיבלנו פונקציה מ-{% equation %}X{% endequation %} אל {% equation %}X{% endequation %} (ולא מ-{% equation %}X{% endequation %} אל "מפה שמתארת את {% equation %}X{% endequation %}").

עכשיו, פונקציה היא <strong>מכווצת</strong> אם היא מקטינה את המרחק בין נקודות, אבל לא סתם ברמה "כלשהי" אלא ברמה שנותנת חסם כפלי כלשהו - "מקטינה פי 2" או "מקטינה פי שבע שמיניות" וכן הלאה. פורמלית צריך להיות קיים קבוע {% equation %}0<q&lt;1{% endequation %} כך שלכל {% equation %}a,b\in X{% endequation %} מתקיים {% equation %}d\left(f\left(a\right),f\left(b\right)\right)\le q\cdot d\left(a,b\right){% endequation %} (באופן כללי פונקציה שבה המרחק בין פלטים של הפונקציה חסום על ידי קבוע <strong>כלשהו</strong> כפול המרחק בין הקלטים נקראת <strong>ליפשיצית</strong>, וכאשר הקבוע הזה קטן מאחד אז היא נקראת "מכווצת"). ומה היה קורה אם לא היה קבוע כזה אלא "סתם" היה מתקיים {% equation %}d\left(f\left(a\right),f\left(b\right)\right)\le d\left(a,b\right){% endequation %} לכל {% equation %}a,b\in X{% endequation %}? ובכן, לא רק שההוכחה שתכף אציג לא הייתה עובדת, גם המשפט כלל לא היה נכון.

אבל מה המשפט בעצם? עוד לא ניסחתי אותו! ובכן, אם {% equation %}f{% endequation %} היא פונקציה מכווצת שכזו ממרחב מטרי שלם לעצמו, אז קיימת נקודה <strong>יחידה</strong> {% equation %}a^{*}\in X{% endequation %} כך ש-{% equation %}f\left(a^{*}\right)=a^{*}{% endequation %}. הפתעה! (טוב, אולי העובדה שהנקודה הזו <strong>יחידה</strong> היא מפתיעה) אבל יותר מכך, אפשר תמיד למצוא אותה באופן הבא: ניקח נקודה {% equation %}a_{0}\in X{% endequation %} באופן <strong>שרירותי לחלוטין</strong> (לא משנה מאיפה נתחיל) ונגדיר סדרה {% equation %}a_{n+1}=f\left(a_{n}\right){% endequation %}, אז מובטח לנו שיתקיים {% equation %}\lim_{n\to\infty}a_{n}=a^{*}{% endequation %} (פורמלית: לכל {% equation %}\varepsilon>0{% endequation %} ממשי קיים {% equation %}N{% endequation %} טבעי כך שאם {% equation %}n>N{% endequation %} אז {% equation %}d\left(a_{n},a^{*}\right)&lt;\varepsilon{% endequation %}). כפי שנראה, אפשר יהיה גם להגיד משהו על <strong>קצב ההתכנסות</strong> של הסדרה הזו אל {% equation %}a^{*}{% endequation %}.

עיקר ההוכחה של המשפט היא חישוב טכני לא נוראי במיוחד של המרחק בין שתי נקודות <strong>כלשהן</strong> בסדרה שכזו. כלומר, נניח ש-{% equation %}n<m{% endequation %} ונחשב חסם עבור {% equation %}d\left(a_{n},a_{m}\right){% endequation %}. הרעיון פה הוא שעבור שתי נקודות שבאות זו אחר זו בסדרה קל לנו לתת חסם מפורש, ואז אפשר להעריך את המרחק בין {% equation %}a_{n}{% endequation %} ו-{% equation %}a_{m}{% endequation %} על ידי שימוש באי-שוויון המשולש כדי לחסום את המרחק ביניהן על ידי נקודות ביניים שהן כל האיברים מ-{% equation %}a_{n}{% endequation %} עד {% equation %}a_{m}{% endequation %}.

נתחיל עם דוגמאות פשוטות: את המרחק {% equation %}d\left(a_{0},a_{1}\right){% endequation %} אין לנו איך לחסום; זו "נקודת המוצא" שלנו. ככל ש-{% equation %}a_{0}{% endequation %} יותר קרוב ל-{% equation %}a_{1}{% endequation %} (כלומר, ככל ש-{% equation %}a_{0}{% endequation %} יותר קרוב אל {% equation %}f\left(a_{0}\right){% endequation %}) כך החסם על ההתכנסות של הסדרה יהיה טוב יותר.

את המרחק {% equation %}d\left(a_{1},a_{2}\right){% endequation %} לעומת זאת אפשר לחסום: {% equation %}a_{1}=f\left(a_{0}\right){% endequation %} ואילו {% equation %}a_{2}=f\left(a_{1}\right){% endequation %} ולכן

{% equation %}d\left(a_{1},a_{2}\right)=d\left(f\left(a_{0}\right),f\left(a_{1}\right)\right)\le qd\left(a_{0},a_{1}\right){% endequation %}

באופן דומה:

{% equation %}d\left(a_{2},a_{3}\right)=d\left(f\left(a_{1}\right),f\left(a_{2}\right)\right)\le qd\left(a_{1},a_{2}\right)\le q^{2}d\left(a_{0},a_{1}\right){% endequation %}

וכבר אפשר להמשיך עם זה באינדוקציה ולקבל את הטענה הכללית שנכונה לכל {% equation %}k\ge0{% endequation %}:

{% equation %}d\left(a_{k},a_{k+1}\right)\le q^{k}d\left(a_{0},a_{1}\right){% endequation %}

חמושים בידע הנוסף הזה אפשר להעריך את {% equation %}d\left(a_{n},a_{m}\right){% endequation %} גם עבור נקודות לא סמוכות. הרעיון הוא להסתכל על כל סדרת הנקודות {% equation %}a_{n},a_{n+1},a_{n+2},\dots,a_{m-1},a_{m}{% endequation %} (הנחנו ש-{% equation %}n<m{% endequation %}) - מאי-שוויון המשולש אנו יודעים שמתקיים

{% equation %}d\left(a_{n},a_{m}\right)\le d\left(a_{n},a_{n+1}\right)+\dots+d\left(a_{m-1},a_{m}\right){% endequation %}

אפשר לכתוב את אותו הדבר בקיצור כך:

{% equation %}d\left(a_{n},a_{m}\right)\le\sum_{i=0}^{m-n-1}d\left(a_{n+i},a_{n+i+1}\right){% endequation %}

וכעת, ממה שמצאנו קודם אנו יודעים ש-{% equation %}d\left(a_{n+i},a_{n+i+1}\right)\le q^{n+i}d\left(a_{0},a_{1}\right){% endequation %} ולכן נקבל

{% equation %}d\left(a_{n},a_{m}\right)\le\sum_{i=0}^{m-n-1}q^{n+i}d\left(a_{0},a_{1}\right)=q^{n}d\left(a_{0},a_{1}\right)\cdot\sum_{i=0}^{m-n-1}q^{i}{% endequation %}

הסכום שנשאר לנו הוא טור הנדסי רגיל. אני תמיד אוהב להזכיר איך אנחנו יודעים מה הסכום של טור הנדסי: אם אני צריך לחשב את {% equation %}1+q+q^{2}+\dots+q^{n}{% endequation %} אני כופל ב-{% equation %}\left(q-1\right){% endequation %} ומקבל הרבה איברים שמצטמצמים ובסוף נשאר {% equation %}q^{n+1}-1{% endequation %}. נחלק ב-{% equation %}q-1{% endequation %} שבו כפלתי, ונקבל שסכום הטור הוא {% equation %}\frac{q^{n+1}-1}{q-1}{% endequation %}. לכן במקרה שלנו:

{% equation %}\sum_{i=0}^{m-n-1}q^{i}=\frac{q^{m-n}-1}{q-1}{% endequation %}

אפשר לפשט את זה טיפה עבורנו - {% equation %}\sum_{i=0}^{m-n-1}q^{i}&lt;\sum_{i=0}^{\infty}q^{i}=\frac{1}{1-q}{% endequation %} (תחשבו שאני מציב 0 במקום {% equation %}q^{m-n}{% endequation %}), ולכן נקבל

{% equation %}d\left(a_{n},a_{m}\right)\le\frac{d\left(a_{0},a_{1}\right)}{1-q}\cdot q^{n}{% endequation %}

וזו כבר תוצאה מצויינת. תזכרו ש-{% equation %}0<q&lt;1{% endequation %}, ולכן ככל ש-{% equation %}n{% endequation %} גדול יותר כך {% equation %}q^{n}{% endequation %} קטן יותר. לכן מה שקיבלנו הוא שהמרחק בין {% equation %}a_{n}{% endequation %} לבין <strong>כל</strong> נקודה שבאה אחריה בסדרה שווה למספר הקבוע {% equation %}\frac{d\left(a_{0},a_{1}\right)}{1-q}{% endequation %} כפול משהו ({% equation %}q^{n}{% endequation %}) שהולך וקטן ככל שאנחנו לוקחים {% equation %}a_{n}{% endequation %} גדול יותר. חישוב לא מסובך מראה שלכל {% equation %}\varepsilon>0{% endequation %} אנחנו מסוגלים למצוא {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} מתקיים {% equation %}\frac{d\left(a_{0},a_{1}\right)}{1-q}\cdot q^{n}&lt;\varepsilon{% endequation %}. כלומר, לכל {% equation %}m>n&gt;N{% endequation %} יתקיים {% equation %}d\left(a_{n},a_{m}\right)&lt;\varepsilon{% endequation %}. זה מראה שהסדרה {% equation %}\left\{ a_{n}\right\} {% endequation %} היא <strong>סדרת קושי</strong>.

סדרת קושי, אינטואיטיבית, היא סדרה שככל שמתקדמים בה יותר כך המרחק בין כל שני איברים בה (לאו דווקא כאלו שסמוכים זה לזה בסדרה) הולך וקטן. פורמלית זה בדיוק מה שתיארנו: לכל {% equation %}\varepsilon{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}m>n&gt;N{% endequation %} מתקיים {% equation %}d\left(a_{n},a_{m}\right)&lt;\varepsilon{% endequation %}. החשיבות של התכונה הזו של "להיות סדרת קושי" היא בכך שהיא מצביעה על כך שהסדרה <strong>אמורה להתכנס</strong> לגבול קונקרטי; כלומר, "צריך" להיות {% equation %}a^{*}{% endequation %} כך שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}d\left(a_{n},a^{*}\right)&lt;\varepsilon{% endequation %}. ה"צריך" הזה לא תמיד מתקיים בפועל; במקרה של {% equation %}\mathbb{R}{% endequation %} הוא מתקיים, אבל במקרה של {% equation %}\mathbb{Q}{% endequation %}, למשל, הוא לאו דווקא מתקיים (תסתכלו על הסדרה {% equation %}3,3.1,3.14,3.141,\dots{% endequation %} ש"אמורה להתכנס אל {% equation %}\pi{% endequation %}" אבל הרי {% equation %}\pi{% endequation %} אינו רציונלי למרות שאברי הסדרה כן). מרחב מטרי שבו כל סדרת קושי היא מתכנסת נקרא <strong>מרחב מטרי שלם</strong>, והנחנו ש-{% equation %}X{% endequation %} הוא מרחב מטרי שלם כחלק מתנאי משפט נקודת השבת של בנך.

לסיכום, הראינו ש-{% equation %}\left\{ a_{n}\right\} {% endequation %} היא סדרת קושי ולכן קיים {% equation %}a^{*}\in X{% endequation %} כך ש-{% equation %}a_{n}\to a^{*}{% endequation %}. אבל מה זה עוזר לנו, בעצם? האם זה מוכיח ש-{% equation %}a^{*}{% endequation %} היא נקודת שבת? ובכן, כן, אבל הנימוק יצריך מאיתנו לראות את היעילות של מושג בסיסי נוסף: <strong>רציפות</strong>.

הנה מה שאני <strong>רוצה</strong> להגיד: אנחנו יודעים ש-{% equation %}\lim_{n\to\infty}a_{n}=a^{*}{% endequation %}. עכשיו, את מהסדרה {% equation %}a_{0},a_{1},a_{2},\dots{% endequation %} אפשר לסלק את האיבר הראשון, ואז לכתוב את הסדרה שנותרה בתור {% equation %}f\left(a_{0}\right),f\left(a_{1}\right),\dots{% endequation %}. כלומר, הסדרות {% equation %}\left\{ a_{n}\right\} {% endequation %} ו-{% equation %}\left\{ f\left(a_{n}\right)\right\} {% endequation %} הן אותה סדרה למעט האיבר הראשון, והאיבר הראשון לא באמת משפיע על גבול הסדרה. לכן גם {% equation %}\lim_{n\to\infty}f\left(a_{n}\right)=a^{*}{% endequation %}.

כעת, הייתי <strong>רוצה</strong> להגיד משהו כזה: {% equation %}\lim_{n\to\infty}f\left(a_{n}\right)=f\left(\lim_{n\to\infty}a_{n}\right){% endequation %}. אם הייתי יכול לומר את זה, אז הייתי מקבל:

{% equation %}a^{*}=\lim_{n\to\infty}f\left(a_{n}\right)=f\left(\lim_{n\to\infty}a_{n}\right)=f\left(a^{*}\right){% endequation %}

מה שהיה מוכיח ש-{% equation %}a^{*}{% endequation %} היא אכן נקודת שבת של {% equation %}f{% endequation %}. אז בואו נתמקד שוב במה שאני <strong>רוצה</strong> שיקרה:

{% equation %}\lim_{n\to\infty}f\left(a_{n}\right)=f\left(\lim_{n\to\infty}a_{n}\right){% endequation %}

במילים: הגבול של סדרת הפלטים של {% equation %}f{% endequation %} על {% equation %}a_{n}{% endequation %} הוא אותו דבר כמו הפלט של {% equation %}f{% endequation %} על הגבול של {% equation %}a_{n}{% endequation %}. הפעולות של "חישוב הגבול של הסדרה" ו"הפעלת {% equation %}f{% endequation %}" הן <strong>קומוטטיביות</strong> - אפשר להחליף את הסדר ביניהן ועדיין לקבל את אותה התוצאה. אם {% equation %}f{% endequation %} היא <strong>פונקציה רציפה</strong> אז הדבר הזה מתקיים. מה זו פונקציה רציפה? בנפנוף ידיים כלשהו - פונקציה שעבור קלטים קרובים מספיק מחזירה פלטים שהם גם כן קרובים.

הנה הגדרה פורמלית: {% equation %}f{% endequation %} רציפה בנקודה {% equation %}x_{0}{% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}\delta>0{% endequation %} כך ש-{% equation %}d\left(x,x_{0}\right)&lt;\delta{% endequation %} ("קלטים קרובים") גורר {% equation %}d\left(f\left(x\right),f\left(x_{0}\right)\right)&lt;\varepsilon{% endequation %} ("פלטים קרובים"). שימו לב שדיברתי פה על רציפות בנקודה <strong>מסויימת</strong>; אומרים על {% equation %}f{% endequation %} שהיא רציפה בכל המרחב {% equation %}X{% endequation %} אם היא רציפה לכל {% equation %}x_{0}\in X{% endequation %}. בהגדרה הזו, ה-{% equation %}\delta{% endequation %} שמוצאים בתגובה ל-{% equation %}\varepsilon{% endequation %} יכול להיות תלוי גם בנקודה {% equation %}x_{0}{% endequation %}; יש הגדרה חזקה יותר של רציפות שנקראת <strong>רציפות במידה שווה</strong> שבה עבור {% equation %}\varepsilon{% endequation %} אפשר למצוא {% equation %}\delta{% endequation %} ש"עובד לכל הנקודות ב-{% equation %}X{% endequation %} בו זמנית"; לא אצטרך את ההגדרה הזו כאן.

רציפות היא תכונה חשובה עם שלל משמעויות שנובעות ממנה, אבל כאן אני אסתפק בזו שרלוונטית לנו: {% equation %}\lim_{n\to\infty}f\left(a_{n}\right)=f\left(\lim_{n\to\infty}a_{n}\right){% endequation %}. כזכור, אנחנו מסמנים {% equation %}a^{*}=\lim_{n\to\infty}a_{n}{% endequation %}, כך שמה שאשתמש בו הוא הרציפות של {% equation %}f{% endequation %} בנקודה {% equation %}a^{*}{% endequation %}. כדי להוכיח {% equation %}f\left(a^{*}\right)=\lim_{n\to\infty}f\left(a_{n}\right){% endequation %} אני לוקח {% equation %}\varepsilon>0{% endequation %} וצריך למצוא {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}d\left(f\left(a^{*}\right),f\left(a_{n}\right)\right)&lt;\varepsilon{% endequation %}. ובכן, מכיוון ש-{% equation %}f{% endequation %} רציפה, קיים {% equation %}\delta>0{% endequation %} כך שאם {% equation %}d\left(a^{*},a_{n}\right)&lt;\delta{% endequation %} אז {% equation %}d\left(f\left(a^{*}\right),f\left(a_{n}\right)\right)&lt;\varepsilon{% endequation %}. כעת, מכיוון ש-{% equation %}a^{*}=\lim_{n\to\infty}a_{n}{% endequation %} אז קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז מתקיים {% equation %}d\left(a^{*},a_{n}\right)&lt;\delta{% endequation %} - ומכאן ש-{% equation %}d\left(f\left(a^{*}\right),f\left(a_{n}\right)\right)&lt;\varepsilon{% endequation %}, כמו שרצינו.

לסיכום: הראינו שאם {% equation %}f{% endequation %} רציפה אז {% equation %}a^{*}{% endequation %} היא אכן נקודת שבת. אבל למה {% equation %}f{% endequation %} רציפה? זו תכונה שמשותפת לכל פונקציה ליפשיצית: אם {% equation %}d\left(f\left(a\right),f\left(b\right)\right)\le q\cdot d\left(a,b\right){% endequation %} עבור {% equation %}0<q{% endequation %} אז בהינתן {% equation %}\varepsilon>0{% endequation %} נבחר {% equation %}\delta=\frac{\varepsilon}{q}{% endequation %} ואז עבור {% equation %}a,b{% endequation %} כך ש-{% equation %}d\left(a,b\right)<\delta{% endequation %} יתקיים

{% equation %}d\left(f\left(a\right),f\left(b\right)\right)\le q\cdot d\left(a,b\right)<q\cdot\frac{\varepsilon}{q}=\varepsilon{% endequation %}

זה מסיים את שלב ה<strong>קיום</strong> של משפט נקודת השבת של בנך. הראינו שאם לוקחים נקודה שרירותית כלשהי ומפעילים את {% equation %}f{% endequation %} עליה שוב ושוב, מתכנסים אל נקודת שבת. למה לא ייתכן שנתכנס אל שתי נקודות שבת שונות אם נתחיל במקומות שונים? הטיעון כאן הוא כמעט טריוויאלי: כי אם {% equation %}f{% endequation %} לא משנה שתי נקודות, אז המרחק בין התמונות שלהן לא יהיה קטן מהמרחק ביניהן, בסתירה לכך ש-{% equation %}f{% endequation %} מכווצת. פורמלית, אם {% equation %}a^{*},b^{*}{% endequation %} הן שתי נקודות שבת אז

{% equation %}d\left(a^{*},b^{*}\right)=d\left(f\left(a^{*}\right),f\left(b^{*}\right)\right)\le qd\left(a^{*},b^{*}\right)\le d\left(a^{*},b^{*}\right){% endequation %}

בפרט, {% equation %}qd\left(a^{*},b^{*}\right)=d\left(a^{*},b^{*}\right){% endequation %} ומכיוון ש-{% equation %}0<q&lt;1{% endequation %} זה קורה רק אם {% equation %}d\left(a^{*},b^{*}\right)=0{% endequation %} כלומר אם {% equation %}a^{*}=b^{*}{% endequation %}. זה מסיים את משפט נקודת השבת של בנך.
<h2>משפט נקודת השבת של ברואר</h2>
משפט נקודת השבת של ברואר אומר שכל פונקציה רציפה מכדור היחידה ה-{% equation %}n{% endequation %} ממדי לעצמו היא בעלת נקודת שבת. ההוכחה שלו היא מסובכת יחסית ולא אציג אותה בפוסט הזה, אבל בואו ננסה להבין במה הוא דומה ושונה למשפט נקודת השבת של בנך.

ראשית, המשפט של ברואר מפורסם יותר ושימושי יותר במתמטיקה, ולכן בכלל הזכרתי אותו למרות שמטרת הפוסט הייתה משפט נקודת השבת של בנך; אני לא חושב שנכון לדבר על משפטי נקודות שבת בלי להזכיר את ברואר בכלל.

שנית, ברואר מדבר על נקודת שבת בפונקציה רציפה <strong>כלשהי</strong>. אצל בנך הדרישה הרבה יותר קיצונית: לא רק שהפונקציה צריכה להיות רציפה, היא צריכה להיות ליפשיצית, עם קבוע ליפשיץ קטן מ-1 ("מכווצת"). במובן זה ברואר מכסה מחלקה רחבה בהרבה של פונקציות.

עוד הבדל, הפעם לטובת בנך, הוא שמשפט בנך תקף במרחב מטרי שלם כלשהו, לא רק במרחב מטרי שחי ב-{% equation %}\mathbb{R}^{n}{% endequation %}. ברואר מתעסק בתנאים מגבילים יותר. אפשר טיפה למתוח את מה שברואר אומר - אם למרחב טופולוגי כלשהו יש את התכונה שלכל פונקציה רציפה מעליו יש נקודת שבת, אז כך גם לכל תמונה הומיאומורפית שלו (מרחב אחר כך שיש בינם התאמה חח"ע ועל שמשמרת את הטופולוגיה של המרחב). זה אומר שאפשר להשתמש בברואר לכל קבוצה קומפקטית קמורה ב-{% equation %}\mathbb{R}^{n}{% endequation %}, אבל עדיין אנחנו "חיים" ב-{% equation %}\mathbb{R}^{n}{% endequation %}; אם תרצו, ברואר הוא אחד ממשפטי האפיון הבסיסיים של "מה זה {% equation %}\mathbb{R}^{n}{% endequation %} בכלל ומה מייחד אותו כמרחב".

ועוד הבדל לטובת בנך הוא שמשפט ברואר הוא לא קונסטרוקטיבי - הוא לא נותן לנו דרך למצוא את נקודת השבת, רק מוכיח שהיא קיימת. זאת בשונה ממשפט בנך, שמראה דרך מפורשת "לבנות" אותה בתור גבול של סדרה. למעשה, העובדה שהמשפט המפורסם שלו עצמו לא קונסטרוקטיבי הייתה אחת מהדברים שגרמו לברואר לאמץ את הגישה ה<strong>אינטואיציוניסטית</strong> לפילוסופיה של המתמטיקה, שבה הוכחות לא קונסטרוקטיביות כאלו אינן מתקבלות בברכה (וכמובן, ראויה לפוסט משל עצמה שמי יודע אם אי פעם אכתוב).

