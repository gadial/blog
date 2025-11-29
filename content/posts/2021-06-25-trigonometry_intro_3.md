---
title: "מה בעצם הולך בטריגונומטריה בתיכון? (חלק ג')"
layout: post
categories:
  - כללי
tags:
  - טריגונומטריה
---


<h2>סינוס וקוסינוס של זווית כפולה</h2>

המטרה שלי בסדרת הפוסטים על טריגונומטריה היא להבין את דף הנוסחאות בטריגו ומאיפה צצו הדברים שמופיעים בו. הנה הוא:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas.png" alt=""/>

בפעם הקודמת הוכחנו בדי הרבה עבודה את שתי הנוסחאות העליונות, עבור סינוס וקוסינוס של סכום/הפרש שתי זוויות. הראיתי שתי דרכים להגיע לנוסחאות הללו: האחת, באמצעות הוכחה גאומטרית לא הכי פשוטה בעולם, והשניה בעזרת משהו מגניב שנקרא <strong>נוסחת אוילר</strong> וגם אם לא מאמינים לו עדיין יכול לשמש בתור כלי נחמד לזכור את הנוסחאות ולקבל אינטואיציה לגבי האופן שבו הן התקבלו.

הפעם אני רוצה לדבר על <strong>ארבע</strong> הנוסחאות הבאות, שעוסקות כולן בסכום והפרש של שני סינוסים או של שני קוסינוסים. אנחנו נראה שכולן מתקבלות בצורה די פשוטה מהנוסחאות שמצאנו בפעם הקודמת; לא נזדקק פה לבניות גאומטריות או לנוסחאות מדהימות עם מספרים מרוכבים. אבל עוד לפני שנגיע לזה, אני רוצה להציג משהו קטן שלא מופיע בדף הנוסחאות שצירפתי וגם לא בדפי נוסחאות רשמיים אחרים שאני מכיר, אבל הוא שימושי ונפוץ - <strong>סינוס וקוסינוס של זווית כפולה</strong>.

הסיבה לכך שזה לא מופיע בדף הנוסחאות היא כנראה שזה מיידי כמעט לחלוטין - כל השאלה היא מה קורה אם בנוסחאות לסכום זוויות אני מציב <strong>את אותה זווית</strong>. כלומר, אם {% equation %}\alpha=\beta{% endequation %}. בואו נראה מה קורה עבור סינוס:

{% equation %}\sin2\alpha=\sin\left(\alpha+\alpha\right)=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha{% endequation %}

ומה קורה עבור קוסינוס:

{% equation %}\cos2\alpha=\cos\left(\alpha+\alpha\right)=\cos\alpha\cos\alpha-\sin\alpha\sin\alpha=\cos^{2}\alpha-\sin^{2}\alpha{% endequation %}

וזהו בעצם - קיבלנו שתי נוסחאות פשוטות יחסית:

<ul> <li>{% equation %}\sin2\alpha=2\sin\alpha\cos\alpha{% endequation %}</li>


<li>{% equation %}\cos2\alpha=\cos^{2}\alpha-\sin^{2}\alpha{% endequation %}</li>

</ul>

בנוסחה לקוסינוס אפשר להתעלל עוד קצת. בפוסט הראשון על טריגו ראינו את <strong>משפט פיתגורס</strong> שהמשמעות שלו עבורנו הייתה ש-{% equation %}\sin^{2}\alpha+\cos^{2}\alpha=1{% endequation %}. אם <strong>נחבר</strong> את הנוסחה הזו לנוסחה של {% equation %}\cos2\alpha{% endequation %} ואז נעביר את 1 אגף, או אם <strong>נחסר</strong> אותה מהנוסחה של {% equation %}\cos2\alpha{% endequation %} ונעביר את 1 אגף, נקבל

<ul> <li>{% equation %}\cos2\alpha=2\cos^{2}\alpha-1{% endequation %}</li>


<li>{% equation %}\cos2\alpha=1-2\sin^{2}\alpha{% endequation %}</li>

</ul>

בשביל מה כל זה טוב? ובכן, מה שמופיע באגף ימין נראה <strong>די מפחיד</strong> אבל מה שמופיע באגף שמאל הוא <strong>די פשוט</strong>. כלומר, השוויון הזה הוא דרך נוחה כדי <strong>לפשט</strong> ביטויים טריגונומטריים. מתי בכלל צריך לפשט ביטויים כאלו? כמובן, כשלומדים טריגונומטריה, אבל לפחות במתמטיקה זה גם קורה פה ושם, מה שהופך את ההיכרות עם קיום הנוסחאות הללו (לא שינון שלהן בעל פה, חלילה) לבעלת תועלת פרקטית כלשהי (ואני לא יודע מה קורה בלימודי הנדסה שונים ומשונים - אני מנחש שצריך את זה יותר שם).

<h2>סכום והפרש של סינוסים וקוסינוסים</h2>

אז איך אני הולך להתמודד עם {% equation %}\sin\alpha+\sin\beta{% endequation %}? התשובה היא שאין לי מושג מה לעשות, אז הלכתי וקראתי. למעשה, זאת הפעם הראשונה מאז שלמדתי בתיכון שקראתי <strong>למה</strong> הנוסחה הזו נכונה ועכשיו אני קצת נעלב כי הטריק הוא כל כך פשוט שאני בטוח שהייתי זוכר אותו עד לימינו אנו אם היו טורחים להראות לי אותו (קרוב לודאי שספר לימודי הטריגונומטריה שלי מהתיכון רוטן עכשיו "היית יכול לקרוא בי כל הזמן, אתה יודע" או משהו).

הטריק הזה הוא שימושי במתמטיקה באופן כללי: אם יש לנו שני מספרים, נאמר {% equation %}a,b{% endequation %}, אז לפעמים נוח מאוד לייצג את שניהם בתור <strong>הממוצע</strong> שלהם ו<strong>המרחק מהממוצע</strong> של כל אחד. הנה דוגמא פשוטה: המספרים {% equation %}5,15{% endequation %}. הממוצע שלהם הוא {% equation %}\frac{5+15}{2}=10{% endequation %} והמרחק של כל אחד מהם מהממוצע הוא 5. זה לא מפתיע שהמרחק הזה זהה עבור שני המספרים - הרעיון בממוצע של שני מספרים הוא בדיוק "המספר שנמצא במרחק זהה משני המספרים".

כדי לחשב את הממוצע של {% equation %}a,b{% endequation %}, כפי שראינו, צריך לחשב את {% equation %}\frac{a+b}{2}{% endequation %}. וכדי לחשב את המרחק מהממוצע? ובכן, נניח ש-{% equation %}a\ge b{% endequation %}, אז בפרט {% equation %}a=\frac{a+a}{2}\ge\frac{a+b}{2}{% endequation %}, כלומר {% equation %}a-\frac{a+b}{2}=\frac{a-b}{2}{% endequation %} הוא מספר חיובי והמרחק של {% equation %}a{% endequation %} מהממוצע; ובדומה, המרחק של {% equation %}b{% endequation %} הוא {% equation %}\frac{a+b}{2}-b=\frac{a-b}{2}{% endequation %}.

אם לסכם, בהינתן {% equation %}a,b{% endequation %} אז הממוצע שלהם הוא {% equation %}\frac{a+b}{2}{% endequation %} והמרחק שלהם מהממוצע הוא {% equation %}\frac{a-b}{2}{% endequation %} . איך זה עוזר לנו פה? ובכן, פשוט מאוד: משני המספרים הללו אנחנו יכולים "לשחזר" את {% equation %}a,b{% endequation %} המקוריים על ידי חיבור וחיסור:

<ul> <li>{% equation %}a=\frac{a+b}{2}+\frac{a-b}{2}{% endequation %}</li>


<li>{% equation %}b=\frac{a+b}{2}-\frac{a-b}{2}{% endequation %}</li>

</ul>

שימו לב שהנוסחה הזו עובדת גם אם {% equation %}b\ge a{% endequation %}; במקרה הזה {% equation %}\frac{a-b}{2}{% endequation %} יהיה מספר שלילי, לא חיובי, ולכן קצת מוזר לקרוא לו "המרחק מהממוצע" כי מרחק הוא בעיקרון מספר אי שלילי. אבל הנוסחה עצמה עדיין עובדת; הדיבור על ממוצע ומרחק הוא פשוט הדרך שלנו לקבל אינטואיציה ראשונית עבורה.

עכשיו, בואו נסתכל על הביטוי שאנחנו מנסים לטפל בו: {% equation %}\sin\alpha+\sin\beta{% endequation %}. הסיבה שקשה לנו לפשט את הביטוי הזה היא שאנחנו לא יודעים איך לקשר בין {% equation %}\sin\alpha{% endequation %} ובין {% equation %}\sin\beta{% endequation %}. אבל אם מתארים את שניהם בשפה המשותפת של הממוצע והמרחק מהממוצע, ומשתמשים בנוסחאות לסכום והפרש זוויות, נקבל ש-{% equation %}\sin\alpha{% endequation %} ו-{% equation %}\sin\beta{% endequation %} יתוארו באמצעות אותה שפה משותפת:

<ul> <li>{% equation %}\sin\alpha=\sin\left(\frac{\alpha+\beta}{2}+\frac{\alpha-\beta}{2}\right)=\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}+\sin\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}{% endequation %}</li>


<li>{% equation %}\sin\beta=\sin\left(\frac{\alpha+\beta}{2}-\frac{\alpha-\beta}{2}\right)=\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}-\sin\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}{% endequation %}</li>

</ul>

אלו כמעט אותם ביטויים! ההבדל היחיד הוא ב<strong>סימן</strong> של המחובר הימני יותר. לכן כשאחבר את שתי השורות המחובר הזה פשוט ייעלם, והמחובר הראשון יופיע פעמיים. אקבל

<ul> <li>{% equation %}\sin\alpha+\sin\beta=2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}{% endequation %}</li>

</ul>

ואם עכשיו <strong>אחסר</strong> את שתי השורות, המחובר <strong>השמאלי יותר</strong> ייעלם בעוד שהימני יופיע פעמיים:

<ul> <li>{% equation %}\sin\alpha-\sin\beta=2\sin\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}{% endequation %}</li>

</ul>

את אותו תעלול אפשר להפעיל גם על קוסינוסים:

<ul> <li>{% equation %}\cos\alpha=\cos\left(\frac{\alpha+\beta}{2}+\frac{\alpha-\beta}{2}\right)=\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}-\sin\frac{\alpha-\beta}{2}\sin\frac{\alpha+\beta}{2}{% endequation %}</li>


<li>{% equation %}\cos\beta=\cos\left(\frac{\alpha+\beta}{2}-\frac{\alpha-\beta}{2}\right)=\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}+\sin\frac{\alpha-\beta}{2}\sin\frac{\alpha+\beta}{2}{% endequation %}</li>

</ul>

כך שעל ידי חיבור וחיסור מתאימים נקבל

<ul> <li>{% equation %}\cos\alpha+\cos\beta=2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}{% endequation %}</li>


<li>{% equation %}\cos\alpha-\cos\beta=-2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}{% endequation %}</li>

</ul>

מאיפה צץ המינוס באגף ימין של {% equation %}\cos\alpha-\cos\beta{% endequation %}? ובכן, זכרו שעבור סכום והפרש זווית של קוסינוסים, הסדר בין הפלוס והמינוס <strong>מתהפך</strong>; דווקא בנוסחה להפרש זוויות מופיע פלוס ובזו של חיבור מופיע מינוס, כך שאם מחסרים את השניה מהראשונה מקבלים שני מינוסים של הביטוי {% equation %}2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}{% endequation %}.

ובכן, סיימנו! הוכחנו ארבע נוסחאות במאמץ די מינימלי! הייתי בטוח שזה יהיה הרבה יותר גרוע. אז לאן עכשיו?

<h2>עוד קצת סגירת קצוות עם חצאי זוויות ומכפלות</h2>

מכיוון שמתחילות להיגמר לי הנוסחאות הטריגונומטריות, חיפשתי דף נוסחאות מקיף יותר:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas3.png" alt=""/>

מה יש פה שלא ראינו קודם? ובכן, ראשית מוזכרת איזו פונקציה מסתורית שנקראת {% equation %}\text{tan}{% endequation %} ("טנגנס") שעד כה נמנעתי מלדבר עליה; נגיע אליה בהמשך. כנ"ל עבור {% equation %}\text{cot}{% endequation %} ("קוטנגנס"). כמו כן יש פה את הנוסחאות שכבר מצאנו לסכום והפרש זוויות, סכום והפרש פונקציות וזווית כפולה. מה שטרם ראינו הוא מה שנקרא "חצי זווית" ומה שנקרא "מכפלת פונקציות" ששניהם מתקבלים בקלות מהדברים שכבר ראינו.

נתחיל עם הנוסחאות לחצי זווית:

<ul> <li>{% equation %}\sin\frac{\alpha}{2}=\pm\sqrt{\frac{1-\cos\alpha}{2}}{% endequation %}</li>


<li>{% equation %}\cos\frac{\alpha}{2}=\pm\sqrt{\frac{1+\cos\alpha}{2}}{% endequation %}</li>

</ul>

הנוסחאות הללו נראות קצת מוזר. מה זאת אומרת {% equation %}\pm{% endequation %}? הרי אלו פונקציות. נותנים להן קלט, הן מחזירות פלט בודד. ובכן, התשובה היא שהנוסחאות הללו לא הכי טובות בעולם; מה שהן בעצם אומרות הוא "{} {% equation %}\sin\frac{\alpha}{2}{% endequation %} הולך להיות שווה בערכו המוחלט ל-{% equation %}\sqrt{\frac{1-\cos\alpha}{2}}{% endequation %} אבל אנחנו לא סגורים על הסימן". אפשר להסיק את הסימן בדרך אחרת, כי אנחנו יודעים בדיוק עבור אילו ערכי {% equation %}\alpha{% endequation %} סינוס הוא חיובי (בין 0 ל-180 מעלות) ועבור אילו הוא שלילי (בין 180 ל-360 מעלות).

איך מגיעים לנוסחאות הללו? בעזרת מה שכבר ראינו על זווית כפולה של <strong>קוסינוס</strong>. כזכור, קיבלנו שתי משוואות עבור אותו דבר:

<ul> <li>{% equation %}\cos2\alpha=2\cos^{2}\alpha-1{% endequation %}</li>


<li>{% equation %}\cos2\alpha=1-2\sin^{2}\alpha{% endequation %}</li>

</ul>

בואו נחליף בהן את {% equation %}2\alpha{% endequation %} ב-{% equation %}\alpha{% endequation %} ובהתאם נחליף את {% equation %}\alpha{% endequation %} ב-{% equation %}\frac{\alpha}{2}{% endequation %}:

<ul> <li>{% equation %}\cos\alpha=2\cos^{2}\frac{\alpha}{2}-1{% endequation %}</li>


<li>{% equation %}\cos\alpha=1-2\sin^{2}\frac{\alpha}{2}{% endequation %}</li>

</ul>

עכשיו נעביר אגפים כך שהביטוי עם ה-{% equation %}\frac{\alpha}{2}{% endequation %} יהיה לבדו בצד אחד. נתחיל דווקא בביטוי השני עם הסינוס:

<ul> <li>{% equation %}2\sin^{2}\frac{\alpha}{2}=1-\cos\alpha{% endequation %}</li>


<li>{% equation %}2\cos^{2}\frac{\alpha}{2}=1+\cos\alpha{% endequation %}</li>

</ul>

ועכשיו נחלק ב-2 ונוציא שורש ונקבל בדיוק את המשוואות שרצינו להגיע אליהן. הוצאת השורש היא זו שמובילה ל-{% equation %}\pm{% endequation %}, אבל שימו לב שאנחנו לא פותרים כאן משוואה - זה לא שגם עבור פלוס וגם עבור מינוס הפתרון הוא לגיטימי. אם אני כותב את השוויון {% equation %}\left(-3\right)^{2}=9{% endequation %} ואז מוציא שורש משני האגפים אני אקבל {% equation %}-3=\pm\sqrt{9}{% endequation %} וכאן המשמעות של הפלוס-מינוס היא בדיוק אי הודאות שהזכרתי קודם; השוויון {% equation %}-3=\sqrt{9}{% endequation %} פשוט לא מתקיים ({% equation %}\sqrt{9}{% endequation %} הוא תמיד הסימן לשורש <strong>החיובי</strong> של 9).

נעבור עכשיו אל הנוסחאות למכפלה של סינוסים וקוסינוסים. יש לנו ארבע מכפלות, אבל למעשה שתי הראשונות, עבור {% equation %}\sin\alpha\cos\beta{% endequation %} ו-{% equation %}\cos\alpha\sin\beta{% endequation %} הן אותו דבר בתחפושת - הרי מה זה משנה אם קראנו בשם {% equation %}\alpha{% endequation %} לקלט שהסינוס מקבל או הקלט שהקוסינוס מקבל? אבל בנוסחה שאנחנו מקבלים בסוף יש חוסר סימטריה כלשהו (משהו במינוס ומשהו אחר לא במינוס) כך שהבחירה כן רלוונטית.

ובכן, כיצד נקבל את {% equation %}\sin\alpha\cos\beta{% endequation %}? זה נראה לי מפחיד במבט ראשון עד שאני נזכר שזה ביטוי שמופיע בפיתוח של {% equation %}\sin\left(\alpha+\beta\right){% endequation %} וגם בפיתוח של {% equation %}\sin\left(\alpha-\beta\right){% endequation %} ובעצם יש לי כאן טריק שדומה למה שהשתמשתי בו קודם עבור סכום והפרש של סינוסים.

אם כן, אני כותב:

{% equation %}\sin\left(\alpha+\beta\right)=\sin\alpha\cos\beta+\cos\alpha\sin\beta{% endequation %}

{% equation %}\sin\left(\alpha-\beta\right)=\sin\alpha\cos\beta-\cos\alpha\sin\beta{% endequation %}

עכשיו, מה אני יכול לעשות עם המשוואות הללו כדי לבודד מתוכן את {% equation %}\sin\alpha\cos\beta{% endequation %}? טריק פשוט - לחבר אותן, ולחלק ב-2. בצורה הזו {% equation %}\cos\alpha\sin\beta{% endequation %} הולך להתבטל משתי המשוואות ונישאר רק עם {% equation %}\sin\alpha\cos\beta{% endequation %}. קיבלנו

<ul> <li>{% equation %}\sin\alpha\cos\beta=\frac{1}{2}\left(\sin\left(\alpha+\beta\right)+\sin\left(\alpha-\beta\right)\right){% endequation %}</li>

</ul>

ואם אני <strong>אחסר</strong> את המשוואה השניה מהראשונה ואחלק ב-2? אני אשאר עם ה-{% equation %}\cos\alpha\sin\beta{% endequation %}:

<ul> <li>{% equation %}\cos\alpha\sin\beta=\frac{1}{2}\left(\sin\left(\alpha+\beta\right)-\sin\left(\alpha-\beta\right)\right){% endequation %}</li>

</ul>

ועכשיו בואו נעבור לסכום והפרש של זוויות של קוסינוסים:

{% equation %}\cos\left(\alpha+\beta\right)=\cos\alpha\cos\beta-\sin\alpha\sin\beta{% endequation %}

{% equation %}\cos\left(\alpha-\beta\right)=\cos\alpha\cos\beta+\sin\alpha\sin\beta{% endequation %}

אז כאן <strong>חיבור</strong> יבודד לנו את קוסינוס-קוסינוס:

<ul> <li>{% equation %}\cos\alpha\cos\beta=\frac{1}{2}\left(\cos\left(\alpha+\beta\right)+\cos\left(\alpha-\beta\right)\right){% endequation %}</li>

</ul>

בעוד ש<strong>חיסור</strong> של המשוואה <strong>הראשונה</strong> מהשניה תיתן לנו את סינוס-סינוס:

<ul> <li>{% equation %}\sin\alpha\sin\beta=\frac{1}{2}\left(\cos\left(\alpha-\beta\right)-\cos\left(\alpha+\beta\right)\right){% endequation %}</li>

</ul>

וזה מסיים עוד מקבץ אימתני של נוסחאות!

מה שנחמד בכל מה שראינו הפעם הוא שאין כאן בעצם שום טריגונומטריה. הכל פה הוא מניפולציות אלגבריות פשוטות יחסית, ודי סטנדרטיות. למה זה יפה? ראשית, כי זה עושה את החיים קלים יחסית. שנית, כי זה עוזר להעריך את הנוסחאות של סינוס וקוסינוס של סכום זוויות - בעצם <strong>הכל</strong> נבע מהן, וזה "מצדיק" את העבודה הקשה יחסית שהשקענו בלהוכיח אותן. בעצם כל ה"עומק" של הפונקציות הטריגונומטריות התחבא בהוכחות הללו.

האם סיימנו? ודאי שלא. עדיין צריך לדבר על "משפט הסינוסים" ועל "משפט הקוסינוסים" שמופיעים בדפי הנוסחאות, שלא לדבר על הטנגנס המסתורי שראינו הפעם. לזה נגיע בפעמים הבאות. 
