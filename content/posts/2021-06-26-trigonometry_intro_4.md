---
title: "מה בעצם הולך בטריגונומטריה בתיכון? (חלק ד' - משפט הסינוסים)"
layout: post
categories:
  - כללי
tags:
  - טריגונומטריה
image: "2021/sine_formula5.png"
description: 'משפט הסינוסים הוא הרגע המטריד שבו הטריגונומטריה מתחילה להיות שימושית בפועל עבור דברים בניגוד לתפיסה הפופולרית שלה כמשהו שמיועד להתעללות באנשים. ספציפית, השיטה של טריאנגולציה שבה מסיקים מרחק אל יעד מתוך שתי נקודות תצפית שהמרחק ביניהן ידוע נובעת ממשפט הסינוסים'
---

אני ממשיך בסדרת הפוסטים שלי על גאומטריה שהמטרה המוצהרת שלה היא להבין את כל הנוסחאות הטריגונומטריות שרואים בבית הספר ומה הרעיון מאחוריהן. הנה דף הנוסחאות שאני עובד איתו:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas.png" alt=""/>

הפעם אני רוצה לדבר על אחת הנוסחאות שקשורות למשולשים ולמעגלים - משפט הסינוסים (ועל הדרך גם הנוסחה לשטח משולש שמופיעה בסוף). שום דבר לא הולך להיות קשה במיוחד אבל נצטרך להתעסק בגאומטריה (!)

זה... לא כל כך נורא, אפילו לאדם כמוני שמבועת משרטוטים גאומטריים. למעשה, מה שנראה הפעם הוא גם סוג של הסבר "למה טריגונומטריה שימושית בעצם" אם כי לא אכנס לעומק הפרטים.

ההגדרה לסינוס שראינו התבססה על <strong>משולש ישר זווית</strong>, כלומר משולש שנראה כך:

<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle.png" alt=""/>

במשולש הזה, {% equation %}\sin\alpha=\frac{a}{c}{% endequation %}, או בניסוח אחר {% equation %}a=c\sin\alpha{% endequation %}. זה אמנם שימושי מאוד, אבל זה גם מעלה את השאלה מה קורה במשולש <strong>כללי</strong>, שאינו ישר זווית. למשל זה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula1.png" alt=""/>

במשולש הזה אין זווית ישרה (אולי {% equation %}\angle ACB{% endequation %} קצת נראית ככה כי אני מאייר גרוע, אבל היא לא), אז לא ברור איך אפשר לקשר סינוסים אליו, אבל האמת היא שבכל משולש מסתתרת זווית ישרה וכדי לחשוף אותה אני רוצה שניזכר לרגע במשהו לכאורה לא קשור - איך מחשבים <strong>שטח</strong> של משולש. הנוסחה היא {% equation %}\frac{ah}{2}{% endequation %} כאשר {% equation %}a{% endequation %} הוא אורך צלע ו-{% equation %}h{% endequation %} הוא אורך <strong>אנך</strong> לאותה צלע. כדי להבין למה הנוסחה נכונה, מה זה אנך ומה הולך פה, בואו נדגים את זה על ידי הורדת אנך מהקודקוד {% equation %}C{% endequation %} אל הצלע {% equation %}AB{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula2.png" alt=""/>

האנך הזה הוא קו ישר שמתחיל ב-{% equation %}C{% endequation %} ויורד על {% equation %}AB{% endequation %} ופוגש את הצלע הזו בזווית ישרה. התוצאה היא שחילקנו את המשולש התמים {% equation %}ABC{% endequation %} לשני משולשים ישרי זווית: {% equation %}ACD{% endequation %} ו-{% equation %}BCD{% endequation %}, מה שמאפשר לסינוסים לחזור בגדול. האם עבור <strong>כל</strong> משולש אפשר לעשות את הקסם הזה? כן ולא; עוד מעט אתייחס למקרה הבעייתי-שאינו-באמת-בעייתי.

ראשית, איך מגיעים מהבניה הזו אל הנוסחה לשטח של משולש? ובכן, הקסם הוא פשוט: מסתתר בתמונה הזו מלבן, וכדאי שנציג אותו במפורש:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula3.png" alt=""/>

מה שטח המלבן הזה? שטח של מלבן הוא מכפלה של אורכי שתי צלעות מאונכות שלו. במקרה שלנו צלע אחת של המלבן היא {% equation %}AB{% endequation %}, כלומר אורכה הוא מה שסימנתי ב-{% equation %}c{% endequation %}; והצלעות האחרות הן מאותו אורך כמו האנך {% equation %}h{% endequation %}. לכן שטח המלבן הוא {% equation %}ch{% endequation %}. שטח <strong>המשולש</strong> הוא חצי מזה, כי אם נסתכל לרגע על המשולש {% equation %}ACD{% endequation %} נראה שהוא מחלק <strong>לחצי</strong> את החלק השמאלי של המלבן - בינו ובין משולש אחר, זהה לו (או כפי שקוראים לזה בגאומטריה וקל להוכיח - <strong>חופף לו</strong>) וכך קורה גם עם המשולש {% equation %}BCD{% endequation %} בחצי הימני. זה מניב את הנוסחה {% equation %}\frac{ch}{2}{% endequation %} עבור השטח.

עכשיו בואו נחזיר את הטריגונומטריה למשחק, על ידי הצגת הזווית {% equation %}\angle BAC=\alpha{% endequation %} במפורש:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula4.png" alt=""/>

מכיוון שהמשולש {% equation %}ACD{% endequation %} הוא ישר זווית והיתר שלו הוא {% equation %}b{% endequation %}, נקבל ש-{% equation %}h=b\sin\alpha{% endequation %}. אם נציב את זה בנוסחת השטח של המשולש נקבל ששטחו הוא {% equation %}\frac{bc\sin\alpha}{2}{% endequation %}.

הנוסחה הזו היא שרירותית בצורה מסויימת - היא מתבססת על הבחירה שלנו להסתכל דווקא על הזווית {% equation %}\alpha{% endequation %} במשולש, ולהגיע ממנה איכשהו לשטח של המשולש שהוא תכונה "גלובלית". היא בעצם אומרת - השטח של המשולש שווה למכפלת אורכי שתי צלעות כלשהן בו, כפול סינוס הזווית שכלואה ביניהן, חלקי 2. אני יכול באותה מידה לעשות את זה גם עבור יתר הבחירות של זוגות של צלעות במשולש. אני אסמן ב-{% equation %}\beta{% endequation %} את הזווית שמול הצלע שאורכה {% equation %}b{% endequation %} וב-{% equation %}\gamma{% endequation %} את הזווית שמול הצלע שאורכה {% equation %}c{% endequation %}, ואקבל:

{% equation %}\frac{bc\sin\alpha}{2}=\frac{ac\sin\beta}{2}=\frac{ab\sin\gamma}{2}{% endequation %}

את הביטוי הזה קל לפשט עוד קצת, על ידי זה שנכפיל את כל האגפים ב-2 ונחלק אותם ב-{% equation %}abc{% endequation %}. נקבל:

{% equation %}\frac{\sin\alpha}{a}=\frac{\sin\beta}{b}=\frac{\sin\gamma}{c}{% endequation %}

אפשר גם לקחת את ההופכי של כל אחד מהאגפים הללו כדי לקבל

<ul> <li>{% equation %}\frac{a}{\sin\alpha}=\frac{b}{\sin\beta}=\frac{c}{\sin\gamma}{% endequation %}</li>

</ul>

הנוסחה האחרונה הזו שהגעתי אליה היא מה שנקרא בדרך כלל <strong>משפט הסינוסים</strong>. הוא אומר: היחס בין אורך צלע במשולש כלשהו ובין סינוס הזווית שמול הצלע הזו הוא תמיד מספר קבוע כלשהו עבור המשולש הזה.

איזה מספר קבוע? אולי זה {% equation %}\pi{% endequation %}? אולי זה {% equation %}e{% endequation %}? אולי זה איזה קבוע מלהיב אחר? ובכן, למרבה הצער, לא. זה לא יכול להיות מספר אחד שקבוע <strong>לכל</strong> המשולשים, כי אם נסתכל על {% equation %}\frac{a}{\sin\alpha}{% endequation %}, הרי {% equation %}a{% endequation %} הוא אורך צלע שיכול להיות גדול כרצוננו, ואילו {% equation %}\sin\alpha{% endequation %} תמיד יהיה מספר בין מינוס 1 ובין 1. לכן {% equation %}\frac{a}{\sin\alpha}{% endequation %} יהיה גודל שתלוי בגודל המשולש. מה שנחמד הוא שזה גודל שאולי לא ציפינו לו במבט ראשון: זה בדיוק הקוטר של <strong>המעגל שחוסם</strong> את המשולש, או בניסוח המקובל

<ul> <li>{% equation %}\frac{a}{\sin\alpha}=\frac{b}{\sin\beta}=\frac{c}{\sin\gamma}=2R{% endequation %}</li>

</ul>

כאשר {% equation %}R{% endequation %} הוא <strong>רדיוס</strong> המעגל החוסם. זו הגרסה המלאה של משפט הסינוסים.

מה זה בכלל מעגל שחוסם משולש? אפשר להראות שלכל שלוש נקודות במישור, קיים בדיוק מעגל יחיד שעובר דרך שלושתן. המעגל שחוסם משולש הוא פשוט המעגל שעובר דרך שלושת הקודקודים של המשולש. במקרה שלנו זה נראה כך:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula5.png" alt=""/>

עכשיו, מה זה "רדיוס"? זה קו שמחבר את מרכז המעגל עם נקודה על המעגל. אלא שבציור למעלה בכלל לא טרחתי לסמן את מרכז המעגל. אז בואו נסמן אותו הפעם ונחבר אותו עם {% equation %}C{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula6.png" alt=""/>

את האורך של הקו {% equation %}CO{% endequation %} החדש הזה אני מסמן ב-{% equation %}R{% endequation %}. זה נחמד, אבל כדי שזה יהיה ממש שימושי עבורי אני צריך <strong>להמשיך</strong> את הקו {% equation %}CO{% endequation %} הזה עד שיגיע גם אל הצד השני של המעגל:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula7.png" alt=""/>

עשיתי פה שני דברים: ראשית, המשכתי את הקו הזה עד שהגיע לנקודה {% equation %}D{% endequation %} בצד השני; הישר {% equation %}CD{% endequation %} שהתקבל נקרא <strong>קוטר</strong> של המעגל ואורכו הוא {% equation %}2R{% endequation %}. שנית, חיברתי את הנקודה {% equation %}D{% endequation %} הזו בקו אל {% equation %}B{% endequation %} ובכך יצרתי משולש חדש, {% equation %}BCD{% endequation %}. למה שאעשה דבר כזה? כי כרגיל, כדי להשתמש בטריגונומטריה אנחנו רוצים לחשוף איזה משולש ישר זווית שמתחבא פה. מה הזווית הישרה במקרה שלנו? זו הזווית {% equation %}\angle CBD{% endequation %}. להוכיח שהיא ישרה מתבסס על משפט בגאומטריה של מעגלים - "זווית היקפית שנשענת על קוטר היא בת {% equation %}90^{\circ}{% endequation %}". בתרגום למה שהולך אצלנו: אם יש לנו משולש שאחת מצלעותיו היא קוטר ושתי הצלעות האחרות מחברות נקודות על המעגל, אז המשולש הוא ישר זווית והקוטר הוא היתר.

במשולש החדש הזה, {% equation %}\frac{a}{2R}{% endequation %} הוא הסינוס של הזווית שמול הצלע מאורך {% equation %}a{% endequation %}, כלומר שמול הצלע {% equation %}BC{% endequation %}, כלומר הזווית {% equation %}\angle CDB{% endequation %}. מה הזווית הזו? ובכן, אני טוען שהיא זהה לזווית {% equation %}\angle CAB{% endequation %} שקראנו לה בשעתו {% equation %}\alpha{% endequation %}. גם זה מתבסס על משפט שנוגע למעגלים - גם הזווית {% equation %}\angle CDB{% endequation %} וגם הזווית {% equation %}\angle CAB{% endequation %} הן זוויות היקפיות שנשענות על אותו מיתר, כלומר על הצלע {% equation %}BC{% endequation %}. זוויות היקפיות כאלו הן <strong>שוות</strong> בתנאי שהן מאותו צד של המיתר, וזה מה שקורה אצלנו.

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula8.png" alt=""/>

זה מסיים את ההוכחה במקרה הזה: {% equation %}\sin\alpha=\frac{\left|BC\right|}{\left|CD\right|}=\frac{a}{2R}{% endequation %} ולכן {% equation %}\frac{a}{\sin\alpha}=2R{% endequation %}, מה שמסיים את מה שרצינו להוכיח.

מה נשאר? רק התייחסות למקרה "בעייתי" שהתעלמתי ממנו קודם. בניתוח שלי של המשולש ה"כללי" {% equation %}ABC{% endequation %} הנחתי במובלע שהאנך שאני מוריד עובר <strong>בתוך</strong> המשולש, ובמשולש קהה זווית זה לא קורה. בואו נראה דוגמא:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula9.png" alt=""/>

במשולש הזה אם אני אוריד אנך מ-{% equation %}A{% endequation %} הוא עדיין יהיה בתוך המשולש, אבל אם אוריד אנך מ-{% equation %}C{% endequation %} הוא ייפול בחוץ. ככה זה נראה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula10.png" alt=""/>

הטריק הקודם שלי לחישוב שטחת עם המלבן היפה שמתחלק לשני זוגות של משולשים חופפים, לא עובד פה. אבל מה שכן קורה הוא שפתאום צצו לנו שני משולשים ישרי זווית: {% equation %}BCD{% endequation %} ו-{% equation %}ADC{% endequation %}. את השטח של שני המשולשים <strong>הללו</strong> קל לי לחשב: הוא {% equation %}\frac{h}{2}\cdot\left|BD\right|{% endequation %} ו-{% equation %}\frac{h}{2}\cdot\left|AD\right|{% endequation %}, בהתאמה. מכיוון שהמשולש {% equation %}BCD{% endequation %} מורכב מאיחוד המשולשים {% equation %}ACB{% endequation %} (המשולש המקורי שלי) ו-{% equation %}ADC{% endequation %}, אני מקבל שהשטח של {% equation %}ACB{% endequation %} שווה ל<strong>הפרש</strong> בין שטחי שני המשולשים האחרים, כלומר הוא

{% equation %}\frac{h}{2}\cdot\left|BD\right|-\frac{h}{2}\cdot\left|AD\right|=\frac{h}{2}\left(\left|BD\right|-\left|AD\right|\right){% endequation %}

ומכיוון ש-{% equation %}\left|BD\right|=\left|AD\right|+\left|AB\right|{% endequation %}, אני מקבל את השטח {% equation %}\frac{h}{2}\left|AB\right|=\frac{hc}{2}{% endequation %}, כפי שרציתי. אבל איך אני יכול לקשר את זה לסינוס של משהו? ובכן, זה טיפה טריקי אבל עדיין מאוד פשוט. בואו נסתכל על הזווית {% equation %}\angle BAC{% endequation %} ששווה ל-{% equation %}\alpha{% endequation %}, ועל הזווית {% equation %}\angle DAC{% endequation %} שמשלימה אותה ל-{% equation %}180^{\circ}{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula11.png" alt=""/>

במשולש ישר הזווית {% equation %}ADC{% endequation %} אפשר להשתמש בסינוסים כרגיל, ולכן נקבל ש-{% equation %}\sin\left(180^{\circ}-\alpha\right)=\frac{h}{b}{% endequation %}. זה משמח מאוד, כי סינוס היא פונקציה סימטרית ביחס לציר של {% equation %}90^{\circ}{% endequation %}, כלומר

<ul> <li>{% equation %}\sin\left(180^{\circ}-\alpha\right)=\sin\alpha{% endequation %}</li>

</ul>

זו משוואה שראינו כבר בפוסט הראשון על טריגונומטריה. כלומר, קיבלנו {% equation %}\sin\alpha=\frac{h}{b}{% endequation %}, כלומר {% equation %}h=b\sin\alpha{% endequation %}, ויחד עם השטח {% equation %}\frac{hc}{2}{% endequation %} של המשולש נקבל את השטח {% equation %}\frac{bc\sin\alpha}{2}{% endequation %} וכאן אנחנו כבר בטריטוריה המוכרת של ההוכחה מתחילת הפוסט. זה מסיים את ההוכחה גם עבור משולש קהה זווית.

לבסוף, אני רוצה לומר משהו קטן על השימושיות של משפט הסינוסים. ראשית, אני <strong>לא יודע</strong> מה השימושיות שלו בעולם האמיתי כי לא יצא לי להשתמש בו מחוץ למתמטיקה. שנית, השימושיות שלו ברורה במובן הבא: אם עבור משולש כלשהו אנחנו יודעים שתי זווית ואורך של צלע כלשהי, אנחנו יכולים להסיק מכך את אורכי כל הצלעות של המשולש. למה? מהיכרות עם שתי זוויות אנחנו מסיקים את השלישית (היא {% equation %}180^{\circ}{% endequation %} פחות שתי האחרות), ולכן אנחנו יכולים לחשב את {% equation %}\frac{\sin\alpha}{a}{% endequation %} עבור הצלע שאורכה {% equation %}a{% endequation %} ידוע לנו והזווית {% equation %}\alpha{% endequation %} שמול הצלע הזה. עכשיו אפשר להסיק את אורכי הצלעות האחרות: למשל, {% equation %}\frac{\sin\alpha}{a}=\frac{\sin\beta}{b}{% endequation %} ולכן {% equation %}b=a\cdot\frac{\sin\beta}{\sin\alpha}{% endequation %}.

שיטה מוכרת למדידת מרחקים שמתבססת על ידע שכזה נקראת <strong>טריאנגולציה</strong>. בשיטה הזו, אם אנחנו רוצים למדוד את המרחק עד לנקודה מסויימת, אנחנו מארגנים לעצמנו <strong>שתי</strong> נקודות תצפית עם מרחק ידוע ביניהן (ההנחה היא שנקודות התצפית קרובות יחסית ולכן קל לדעת את המרחק ביניהן ולעומת זאת הנקודה שאת המרחק אליה רוצים למדוד היא מרוחקת). כעת, בעזרת מכשיר מתאים ניתן למדוד את <strong>הזווית</strong> משתי נקודות התצפית אל הנקודה שצופים עליה, וזאת ביחס לקו הישר שמחבר את שתי נקודות התצפית. הנה איור עקום שלי להמחשה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sine_formula12.png" alt=""/>

כאן יש לנו סירה בים, ושני נקודות תצפית בנמל שלנו, אחת על המזח הימני והשניה על המזח השמאלי. המרחק ביניהם ידוע, ולכן מדידת הזווית אל הסירה מכל אחד מהמזחים תאפשר לנו להסיק את מרחק הסירה מכל אחד מהם.כמובן, אם המזחים קרובים יחסית ההפרש בזווית יהיה קטן (התמונה שלי <strong>מאוד</strong> לא ריאליסטית) ולכן מכשירי המדידה שלנו יצטרכו להיות מדויקים יחסית כדי לקבל תוצאה שאפשר לעבוד איתה.

זה מסיים עם משפט הסינוסים; בפוסט הבא נגיע אל <strong>משפט הקוסינוסים</strong> שממש לא דומה בכלל למשפט הסינוסים, אבל גם כן מספק לנו מידע על משולשים כלליים בעזרת הפונקציות הטריגונומטריות. 
